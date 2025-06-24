# 🎬 Movie Recommendation System

This is a Streamlit-based Movie Recommendation System that suggests top 5 movies using **Content-Based Filtering** and **Collaborative Filtering** approaches. It is built using Python, Streamlit, scikit-learn, and scikit-surprise.

---

## 📌 Features

- 🔍 Search by movie title
- ✅ Content-Based Filtering using genres
- 🤝 Collaborative Filtering using SVD (Singular Value Decomposition)
- 🎨 Clean UI with custom styling
- 🧠 Recommends Top 5 Similar Movies
- 💬 (Optional) Sentiment-based filtering with reviews *(planned for future)*

---

## 🗂️ Folder Structure

movie-recommender/
│
├── data/
│ ├── movies.csv # Preprocessed movie data
│ └── ratings.csv # User ratings
│
├── app.py # All-in-one Streamlit app file
├── convert_dataset.py # Converts raw u.data and u.item to CSV (optional)
├── README.md # Project documentation
└── requirements.txt # Python dependencies

yaml
Copy

---

## 📦 Installation & Setup

python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:

pip install -r requirements.txt
Run the app:

streamlit run app.py
📁 Datasets Used
We used the MovieLens 100K Dataset available on Kaggle or GroupLens. If you're using the raw u.data and u.item files, use the convert_dataset.py to generate the required CSVs:


python convert_dataset.py
This will generate:

data/movies.csv

data/ratings.csv

⚙️ How it Works
1. Content-Based Filtering
Uses TF-IDF Vectorizer on genres.

Calculates cosine similarity between movies.

Recommends movies most similar in genre to the input movie.

2. Collaborative Filtering
Uses SVD algorithm from scikit-surprise.

Predicts user ratings for movies not yet rated.

Recommends top predicted movies for a given user ID.

✨ Example
When a user enters “Toy Story”, the app returns 5 similar movies based on genre and user preferences.

🧪 Sample Input Movies
You can try:

Toy Story

GoldenEye

Jumanji

Seven

Braveheart

Apollo 13

Batman Forever

Heat

Casablanca

Star Wars

✅ Dependencies
txt
Copy
streamlit
pandas
numpy
scikit-learn
scikit-surprise
Install them manually if needed:


