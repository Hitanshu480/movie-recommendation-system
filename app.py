import pickle
import streamlit as st
import requests
import os
from concurrent.futures import ThreadPoolExecutor

# ✅ MUST be first
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")


# ✅ LOAD DATA (cached in memory)
@st.cache_resource
def load_data():
    movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    return movies, similarity


movies, similarity = load_data()


# ✅ POSTER FETCH (FAST + SAFE)
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):

    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        return "https://via.placeholder.com/300x450?text=No+API+Key"

    try:
        url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}?api_key={api_key}&language=en-US"

        # ⭐ LOWER timeout = no freezing
        response = requests.get(url, timeout=2)

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            # ⭐ SMALLER image = MUCH faster
            return "https://image.tmdb.org/t/p/w185/" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=Error"


# ✅ PARALLEL RECOMMENDATION (SUPER FAST)
def recommend(movie):

    try:
        index = movies[movies['title'] == movie].index[0]
    except:
        st.error("Movie not found.")
        return [], []

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    movie_ids = [movies.iloc[i[0]]['id'] for i in distances]
    names = [movies.iloc[i[0]]['title'] for i in distances]

    # ⭐ THIS IS THE BIG SPEED BOOST
    with ThreadPoolExecutor() as executor:
        posters = list(executor.map(fetch_poster, movie_ids))

    return names, posters


# ✅ DROPDOWN
selected_movie = st.selectbox(
    "Type or select a movie:",
    movies['title'].values
)


# ✅ BUTTON
if st.button('Show Recommendation'):

    with st.spinner("Fetching recommendations... 🎬"):

        names, posters = recommend(selected_movie)

    if names:

        cols = st.columns(5)

        for col, name, poster in zip(cols, names, posters):
            col.image(poster)
            col.caption(name)
