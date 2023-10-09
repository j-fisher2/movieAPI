import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')

def fetch_movie_poster(movie_title):
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}")

    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            
            poster_path = data["results"][0]["poster_path"]
            # Base URL for TMDb poster images
            base_url = "https://image.tmdb.org/t/p/"
            poster_size = "w500"
            
            complete_poster_url = f"{base_url}{poster_size}{poster_path}"
            return complete_poster_url
        else:
            return None
    else:
        print("Error: Unable to fetch movie details")
        return None

def download_movie_poster(movie_title):
    poster_url = fetch_movie_poster(movie_title)
    if poster_url:
        response = requests.get(poster_url)

        if response.status_code == 200:
            # Save the poster image locally
            with open(f"{movie_title}_poster.jpg", "wb") as f:  #open file for write
                f.write(response.content)
        else:
            print("Error: Unable to fetch poster image")
    else:
        print("No movie poster found for the given title.")


movie_title="transformers"
download_movie_poster(movie_title)
