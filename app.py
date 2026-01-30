import pickle
import streamlit as st
import requests
import os
from concurrent.futures import ThreadPoolExecutor

# PAGE CONFIG
st.set_page_config(page_title="AI Movie Recommender", layout="wide")

st.title("🎬 AI Movie Recommender")
st.write("Discover movies you’ll love based on intelligent similarity.")


# LOAD DATA
@st.cache_resource
def load_data():
    movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    return movies, similarity


movies, similarity = load_data()


# FETCH FULL MOVIE DETAILS
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):

    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        st.error("API key missing. Add TMDB_API_KEY in Streamlit secrets.")
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        poster = (
            "https://image.tmdb.org/t/p/w342/" + data['poster_path']
            if data.get('poster_path')
            else None
        )

        overview = data.get("overview", "No description available.")

        rating = data.get("vote_average", "N/A")

        tmdb_link = f"https://www.themoviedb.org/movie/{movie_id}"

        return poster, overview, rating, tmdb_link

    except:
        return None


# RECOMMEND FUNCTION (FAST - Parallel Calls)
def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    movie_ids = [movies.iloc[i[0]]['id'] for i in distances]
    names = [movies.iloc[i[0]]['title'] for i in distances]

    with ThreadPoolExecutor():
        details = list(map(fetch_movie_details, movie_ids))

    return names, details


# DROPDOWN
selected_movie = st.selectbox(
    "Type or select a movie:",
    movies['title'].values
)


# BUTTON
if st.button('Show Recommendation'):

    with st.spinner("Finding great movies for you... 🍿"):

        names, details = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, movie_data in zip(cols, names, details):

        if movie_data is None:
            continue

        poster, overview, rating, tmdb_link = movie_data

        with col:
            if poster:
                st.image(poster)

            st.subheader(name)
            st.caption(f"⭐ Rating: {rating}")

            st.write(overview[:120] + "...")

            st.markdown(f"[View Details]({tmdb_link})")
