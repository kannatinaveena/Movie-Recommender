import streamlit as st
from recommender import get_recommendations

# Page configuration
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# Custom CSS

st.markdown("""
    <style>
    body {
        background-color: #0000FF;
    }
    .stApp {
        background-color:  #7FFFD4 ;
        padding: 2rem;
        border-radius: 12px;
    }
    .title {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        color: #ff4b4b;
        margin-top: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 40px;
        color: #333;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
    }
            
    </style>
""", unsafe_allow_html=True)

# UI content
st.markdown("<div class='title'>🎥 Movie Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Get personalized suggestions based on your favorite movie 🎞️</div><br>", unsafe_allow_html=True)

# Input from user
movie_name = st.text_input("Enter your favorite movie title:")

if st.button("🔍 Recommend"):
    if movie_name:
        with st.spinner("Finding similar movies..."):
            results = get_recommendations(movie_name)
            st.subheader("✨ Top Recommendations:")
            for i, movie in enumerate(results, 1):
                st.markdown(f"**{i}. {movie}**")
    else:
        st.warning("⚠️ Please enter a movie name.")
