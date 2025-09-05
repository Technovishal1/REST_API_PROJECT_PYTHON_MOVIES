import requests
import pandas as pd   # Needed for Timestamp
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
# Get API key safely
API_KEY = os.getenv("TMDB_API_KEY")

#API_KEY = "7c8c94a5ebfe9983732611c360c1ed25"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

def fetch_movies(language="hi", pages=5):
    """Fetch movies from TMDB for a given language"""
    movies = []

    for page in range(1, pages+1):
        params = {
            "api_key": API_KEY,
            "language": "en-US",
            "with_original_language": language,
            "sort_by": "vote_average.desc",
            "vote_count.gte": 50,
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "results" in data:
            for movie in data["results"]:
                movie_id = movie["id"]
                # Fetch full movie details + credits
                details = requests.get(
                    f"https://api.themoviedb.org/3/movie/{movie_id}",
                    params={"api_key": API_KEY, "append_to_response": "credits"}
                ).json()

                # Director, Producer, Music
                director = "N/A"
                producer = "N/A"
                music = "N/A"
                if "credits" in details and "crew" in details["credits"]:
                    for member in details["credits"]["crew"]:
                        if member["job"] == "Director":
                            director = member["name"]
                        elif member["job"] == "Producer" and producer == "N/A":
                            producer = member["name"]
                        elif member["job"] == "Original Music Composer":
                            music = member["name"]

                # Studio
                studio = details["production_companies"][0]["name"] if details.get("production_companies") else "N/A"

                # Overview
                overview = details.get("overview", "N/A")

                # Append movie to list with all details
                movies.append({
                    "title": movie.get("title"),
                    "rating": movie.get("vote_average"),
                    "language": language,
                    "release_date": movie.get("release_date"),
                    "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None,
                    "director": director,
                    "producer": producer,
                    "music": music,
                    "studio": studio,
                    "overview": overview,
                    "timestamp": pd.Timestamp.now()
                })

    # Return after all pages are processed
    return movies
