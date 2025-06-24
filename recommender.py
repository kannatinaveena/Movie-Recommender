import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv("data/movies.csv")

# Fill missing genres if any
movies["genres"] = movies["genres"].fillna("")

# Vectorize genres using TF-IDF
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create reverse map of indices and movie titles
indices = pd.Series(movies.index, index=movies["title"].str.lower()).drop_duplicates()

def get_recommendations(title, top_n=5):
    title = title.lower()
    if title not in indices:
        return ["❌ Movie not found. Please check your spelling."]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    
    movie_indices = [i[0] for i in sim_scores]
    return movies["title"].iloc[movie_indices].tolist()
