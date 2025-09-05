import pandas as pd
from datetime import datetime

def process_movies(movies, language_name):
    """Convert raw movie JSON into DataFrame and pick top 5"""
    df = pd.DataFrame(movies)

    # Rename raw API fields if they exist
    df.rename(columns={
        "vote_average": "rating",
        "poster_path": "poster"
    }, inplace=True, errors="ignore")

    # Add/overwrite fields
    df["language"] = language_name
    df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ensure all required columns exist
    required_cols = [
        "title", "rating", "language", "release_date", "poster",
        "director", "producer", "music", "studio", "overview", "timestamp"
    ]
    for col in required_cols:
        if col not in df.columns:
            df[col] = "N/A"

    # Pick top 5 by rating
    return df[required_cols].sort_values(by="rating", ascending=False).head(6)
