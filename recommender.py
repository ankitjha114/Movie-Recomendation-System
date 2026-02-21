import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "a40f4623584a998114b2d00ebbfa566c"

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a40f4623584a998114b2d00ebbfa566c"
        )
        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie, user_genres=None):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    scored_movies = list(enumerate(distances))

    # Boost score if movie contains user's favorite genre
    if user_genres:
        for i in range(len(scored_movies)):
            movie_genres = movies.iloc[i]['tags']
            if any(genre in movie_genres for genre in user_genres):
                scored_movies[i] = (i, scored_movies[i][1] + 0.2)

    movies_list = sorted(
        scored_movies,
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

def get_popular_anime():
    url = "https://graphql.anilist.co"

    query = '''
    query {
      Page(perPage: 50) {
        media(type: ANIME, sort: POPULARITY_DESC) {
          id
          title {
            romaji
          }
        }
      }
    }
    '''

    response = requests.post(url, json={'query': query})
    data = response.json()

    anime_list = []
    for anime in data['data']['Page']['media']:
        anime_list.append(anime['title']['romaji'])

    return anime_list
