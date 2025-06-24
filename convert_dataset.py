import pandas as pd

# Load u.item (movie info)
movies = pd.read_csv(
    "data/ml-100k/u.item", 
    sep="|", 
    encoding="latin-1", 
    header=None,
    usecols=[0, 1, 2],  # movieId, title, release_date
    names=["movieId", "title", "release_date"]
)
# Add dummy genres if not available
movies["genres"] = "Unknown"

# Save to movies.csv
movies[["movieId", "title", "genres"]].to_csv("data/movies.csv", index=False)
print("✅ Created: data/movies.csv")

# Load u.data (ratings info)
ratings = pd.read_csv(
    "data/ml-100k/u.data",
    sep="\t",
    header=None,
    names=["userId", "movieId", "rating", "timestamp"]
)

# Save to ratings.csv (drop timestamp)
ratings[["userId", "movieId", "rating"]].to_csv("data/ratings.csv", index=False)
print("✅ Created: data/ratings.csv")
