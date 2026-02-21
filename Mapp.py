import streamlit as st
from recommender import recommend, movies
from database import register_user, add_watch_history
from anime_recommender import recommend_anime, get_popular_anime

st.set_page_config(page_title="CineMatch", layout="wide")

# Custom Netflix Dark Theme
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }

    /* Main Titles */
    h1, h2, h3 {
        color: #E50914;
        text-align: center;
    }

    /* Fix Form Labels */
    label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    /* Input Boxes */
    input, textarea {
        background-color: #1f1f1f !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 6px !important;
    }

    /* Select & Multiselect */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1f1f1f !important;
        color: white !important;
        border-radius: 6px !important;
    }

    /* Number input */
    .stNumberInput input {
        background-color: #1f1f1f !important;
        color: white !important;
    }

    /* Button */
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 180px;
        font-weight: bold;
        border: none;
    }

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center;">
        <h1> System is ML integrated</h1>
        <p style="color:gray;">Your Personal AI Movie Recommender</p>
    </div>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Movie Recommender", layout="wide")

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("Welcome to Recomeation System")


    with st.form("login_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        mobile = st.text_input("Mobile Number")
        age = st.number_input("Age", min_value=10, max_value=100)
        genres = st.multiselect(
            "Favorite Genres",
            ["Action", "Comedy", "Drama", "Sci-Fi", "Romance", "Thriller"]
        )

        submit = st.form_submit_button("Create Account")

        if submit:
            register_user(name, email, mobile, age, genres)
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.user_genres = genres
            st.success("Login Successful")
            st.rerun()

# MAIN APP
else:
    #st.title("Recomendation System")

    content_type = st.radio("Select Recommendation Type", ["Movies", "Anime"])

    if content_type == "Movies":
        selected_movie = st.selectbox("Select a Movie", movies['title'].values)

        if st.button("Recommend Movies"):
            names, posters = recommend(selected_movie)

            cols = st.columns(5)
            for i in range(5):
                with cols[i]:
                    st.image(posters[i])
                    st.markdown(f"**{names[i]}**")
    else:
        anime_titles = get_popular_anime()
        selected_anime = st.selectbox("Select an Anime", anime_titles)
        if st.button("Recommend Anime"):
            results = recommend_anime(selected_anime)
            if results:
                cols = st.columns(5)
                for i, (title, poster) in enumerate(results):
                    with cols[i]:
                        st.image(poster)
                        st.markdown(f"**{title}**")
            else:
                st.error("Anime not found")