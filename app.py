import streamlit as st
import pickle
import pandas as pd
import requests

# --- Page Setup ---
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    h1, h2 {
        text-align: center;
        color: #ffffff;
    }

    /* Instruction text */
    .instruction {
        text-align: center;
        font-size: 18px;
        color: #ffffff;
        margin-bottom: 20px;
    }

    /* Label for selectbox */
    .movie-label {
        display: block;
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 10px;
    }

    /* Center selectbox */
    div[data-baseweb="select"] {
        margin: 0 auto;
        width: 60%;
    }

    /* Big Recommend button with backside glow */
    div.stButton > button:first-child {
        background-color: #1E90FF;
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        width: 60%;
        display: block;
        margin: 15px auto;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 20px rgba(30, 144, 255, 0.4);
    }

    div.stButton > button:first-child:hover {
        box-shadow: 0 0 35px rgba(30, 144, 255, 0.8);
        transform: scale(1.03);
    }

    /* Movie card */
    .movie-card {
        text-align: center;
        background-color: #111;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s ease;
    }

    .movie-card img {
        width: 160px;
        height: 240px;
        border-radius: 10px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        object-fit: cover;
    }

    /* Hover effect (Purple Glow + Slight Zoom) */
    .movie-card:hover img {
        transform: scale(1.1);
        box-shadow: 0 0 25px rgba(138, 43, 226, 0.9);
        border: 2px solid rgba(138, 43, 226, 0.7);
        z-index: 10;
    }

    .movie-title {
        margin-top: 8px;
        font-size: 15px;
        color: #e0d8ff;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Title ---
st.markdown("<h1>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<div class='instruction'>Select a movie to get the top 5 similar recommendations with posters.</div>", unsafe_allow_html=True)

# --- Load Data ---
try:
    movies = pd.read_csv("tmdb_5000_movies.csv")  # Must contain 'title' and 'id' columns
    similarity = pickle.load(open("similarity.pkl", "rb"))
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# --- Fetch Poster Function ---
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return None
    except:
        return None

# --- Recommend Function ---
def recommend(movie_name):
    idx = movies[movies["title"] == movie_name].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    rec_names, rec_posters = [], []
    for i in sim_scores:
        movie_id = movies.iloc[i[0]]["id"]
        rec_names.append(movies.iloc[i[0]]["title"])
        rec_posters.append(fetch_poster(movie_id))
    return rec_names, rec_posters

# --- Movie Selection ---
st.markdown("<label class='movie-label'>Choose a movie:</label>", unsafe_allow_html=True)
selected_movie = st.selectbox("", movies["title"].values)

# --- Recommend Button ---
if st.button("Recommend Movies"):
    names, posters = recommend(selected_movie)
    st.session_state["rec_names"] = names
    st.session_state["rec_posters"] = posters

# --- Show Recommendations ---
if "rec_names" in st.session_state:
    names = st.session_state["rec_names"]
    posters = st.session_state["rec_posters"]

    if names:
        st.markdown("<h2>Top 5 Recommendations</h2>", unsafe_allow_html=True)
        cols = st.columns(5)
        for i in range(len(names)):
            with cols[i]:
                st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
                if posters[i]:
                    st.image(posters[i], use_container_width=False)
                st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found.")
