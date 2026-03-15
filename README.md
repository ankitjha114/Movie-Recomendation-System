**CineMatch AI – Movie & Anime Recommendation System**

CineMatch AI is a Machine Learning based recommendation system that suggests movies and anime based on content similarity. The project uses basic ML concepts, natural language processing, and similarity algorithms to recommend similar content to users.
The system analyzes movie metadata such as genres, keywords, cast, and overview to calculate similarity between movies. When a user selects a movie, the model finds and recommends the most similar movies.
The application is deployed using Streamlit, providing a clean and interactive user interface.


**Features**

1.Movie Recommendation System
2.Anime Recommendation using AniList API
3.Content-based filtering using ML
4.Netflix-style dark UI
5.Movie & Anime posters using APIs
6.Dropdown selection for easy searching
7.Fast similarity search using cosine similarity
8.Interactive web app using Streamlit


**Machine Learning Concepts Used**

This project is based on Content-Based Filtering, a common recommendation technique used by platforms like Netflix and Spotify.

The main ML concepts used are:
1.Natural Language Processing (NLP)
2.Feature Engineering
3.Vectorization
4.Cosine Similarity
5.Data Preprocessing
6.The system compares movie metadata and recommends content with similar characteristics.


**Python Libraries Used**

The project uses several Python libraries to handle data processing, machine learning, and web interface.
Core Libraries
Library	Purpose
1.pandas	Data manipulation and dataset handling
2.numpy	Numerical operations
3.scikit-learn	Machine learning utilities
4.nltk	Natural language processing and stemming
5.ast	Converting stringified lists into Python objects
6.pickle	Saving trained models and processed data
7.Web App Libraries
8.Library	Purpose
9.streamlit	Building the interactive web application
10.requests	Fetching movie/anime posters from APIs


**Dataset Used**

The dataset used for movies is the TMDB 5000 Movie Dataset.

Files used:
tmdb_5000_movies.csv
tmdb_5000_credits.csv
These datasets contain information about:
1.Movie titles
2.Genres
3.Cast
4.Crew
5.Keywords
6.Overview


**Step-by-Step Working Process**

1️ Data Collection
The project begins by loading the movie dataset:
tmdb_5000_movies.csv
tmdb_5000_credits.csv
These datasets contain important information required for recommendations.

2️ Data Preprocessing
The datasets are merged using the movie title as a common column.
Important columns are selected:
1.movie_id
2.title
3.overview
4.genres
5.keywords
6.cast
7.crew
This helps reduce unnecessary data and focuses only on useful features.

3️ Feature Engineering
The selected features are combined to create a single text feature called tags.
Example:
tags = overview + genres + keywords + cast + crew

This combined text helps the model understand the movie context.

4️ Data Cleaning
Before training the model:
1.Spaces are removed
2.Text is converted to lowercase
3.Missing values are handled
4.JSON formatted columns are converted using ast.literal_eval
This ensures clean and usable data.

5️ Text Vectorization
The text data is converted into numerical form using:
CountVectorizer
Example:
CountVectorizer(max_features=5000, stop_words='english')

This converts text into a bag-of-words vector representation.

6️ Stemming
Stemming reduces words to their root form.
Example:
loved → love
loving → love
This improves similarity matching.
Library used:
nltk.PorterStemmer

7️ Similarity Calculation
After vectorization, the similarity between movies is calculated using:
cosine_similarity()
Cosine similarity measures how similar two movies are based on their feature vectors.

8️ Building the Recommendation Function
A recommendation function is created that:
Finds the selected movie index
Calculates similarity scores
Sorts movies by similarity
Returns the top 5 similar movies

9️ Saving the Model
To avoid recalculating everything every time, the processed data is saved using:
pickle
Files saved:
movies.pkl
similarity.pkl
These files are loaded in the web application.

10 Building the Web Application
The user interface is created using Streamlit.
Features include:
1.Movie selection dropdown
2.Recommendation button
3.Poster display
4.Anime recommendation integration
5.Dark Netflix-style theme
6.Users can simply select a movie and get recommendations instantly.


**Anime Recommendation Integration**

The project also integrates AniList API to recommend anime.
Using GraphQL queries, the system fetches:
1.Anime titles
2.Genres
3.Cover images
These are displayed alongside movie recommendations.


**Project Output**

When a user selects a movie or anime:
The system displays:
1.Recommended titles
2.Posters
3.Similar content suggestions
This creates an interactive recommendation experience.


**Project Structure**

Movie-Recommendation-System
│
├── Mapp.py
├── recommender.py
├── anime_recommender.py
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md

--> **How to Run the Project**
1️ Clone the Repository
git clone https://github.com/your-username/cinematch-ai.git
2️ Install Required Libraries
pip install -r requirements.txt
or manually install:
pip install pandas numpy scikit-learn nltk streamlit requests
3️ Run the Application
streamlit run Mapp.py
The app will open in your browser:
http://localhost:8501


**Future Improvements**

Possible upgrades for the project:
1.User based collaborative filtering
2.Personalized recommendations
3.Watch history tracking
4.Movie rating integration
5.Trailer preview
6.Deployment on cloud platforms


**Author**

Ankit Kumar Jha

Machine Learning Enthusiast | AI Developer | Python Programmer
