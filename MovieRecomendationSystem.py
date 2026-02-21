import numpy as np
import pandas as pd
import ast

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

#print(movies.head())
#print(movies.head(1))
#print(credits.head())
#print(credits.head(1))
#print(credits.head(1)['cast'].values)
#print(credits.head(1)['crew'].values)

movies = (movies.merge(credits, on='title'))
#print(movies.merge(credits, on='title').shape)
print(movies.head(1))
print(movies.shape)
print(credits.shape)

# genres, id, keywords, title, overview, cast, crew
print(movies['original_language'].value_counts())
print(movies.info())

movies = (movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']])
print(movies.head())
#print(movies.isnull().sum())
print(movies.dropna(inplace=True))
print(movies.isnull().sum())
print(movies.duplicated().sum())
#print(movies.iloc[0])
print(movies.iloc[0].genres)

# [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]
# but we want this Format: 'Action', 'Adventure', 'Fantasy'. So we can do this-

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
print(movies.head())
#convert([{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]) # Throws Error that string indices must be integers
# But if we use ast function it will be automatically convert into integers
# print(ast.literal_eval([{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]))
movies['keywords'] = (movies['keywords'].apply(convert))
print(movies.head())
#print(movies['cast'][0])
def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L
movies['cast'] = (movies['cast'].apply(convert3))
print(movies.head())

#print(movies['crew'][0])
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L
movies['crew'] = (movies['crew'].apply(fetch_director))
print(movies.head())
#print(movies['overview'][0])
movies['overview'] = (movies['overview'].apply(lambda x:x.split()))
print(movies.head())
movies['genres'] = (movies['genres'].apply(lambda x:[i.replace(" ", "") for i in x]))
movies['keywords'] = (movies['keywords'].apply(lambda x:[i.replace(" ", "") for i in x]))
movies['cast'] = (movies['cast'].apply(lambda x:[i.replace(" ", "") for i in x]))
movies['crew'] = (movies['crew'].apply(lambda x:[i.replace(" ", "") for i in x]))
print(movies.head())
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
print(movies.head())
new_df = movies[['movie_id', 'title', 'tags']]
#print(new_df)
new_df['tags'] = (new_df['tags'].apply(lambda x:" ".join(x)))
print(new_df.head())

import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags'] = (new_df['tags'].apply(stem))

print(new_df['tags'][0])
print(new_df['tags'][1])
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())
print(new_df.head())

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = (cv.fit_transform(new_df['tags']).toarray())
#print(cv.fit_transform(new_df['tags']).toarray().shape)
print(vectors)
print(vectors[0])
print(cv.get_feature_names_out())
print(len(cv.get_feature_names_out()))


#print(ps.stem('loved'))
print(stem('In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. Action Adventure Fantasy ScienceFiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d SamWorthington ZoeSaldana SigourneyWeaver JamesCameron'))

from sklearn.metrics.pairwise import cosine_similarity
similarity = (cosine_similarity(vectors))
#print(cosine_similarity(vectors).shape)
print(similarity)
print(similarity.shape)
print(similarity[0])
print(similarity[0].shape)

#print(sorted(similarity[0]))
#print(sorted(similarity[0])[-1])
#print(sorted(similarity[0])[-10:-1])
#print(sorted(similarity[0],reverse=True))
#print(list(enumerate(similarity[0])))
#print(sorted(list(enumerate(similarity[0]))))
#print(sorted(list(enumerate(similarity[0])),reverse=True))
#print(sorted(list(enumerate(similarity[0])),reverse=True, key=lambda x:x[1]))
#print(sorted(list(enumerate(similarity[0])),reverse=True, key=lambda x:x[1])[1:6])

# For Recomendation to work
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = (sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6])

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

#print(new_df['title'] == 'Avatar')
# print(new_df[new_df['title'] == 'Avatar'])
# print(new_df[new_df['title'] == 'Avatar'].index[0])
# print(new_df[new_df['title'] == 'Batman'].index[0])

(recommend('Avatar'))
(recommend('Batman Begins'))

import pickle
#print(pickle.dump(new_df, open('movies.pkl', 'wb')))
new_df = movies[['movie_id', 'title', 'genres', 'tags']]
print(pickle.dump(new_df.to_dict(), open('movies.pkl', 'wb')))
print(pickle.dump(similarity, open('similarity.pkl', 'wb')))