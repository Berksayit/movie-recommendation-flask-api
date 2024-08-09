import os

Config = { 
    "OMDB_API_KEY": os.getenv("OMDB_API_KEY"),
    "OMDB_API_URL": "http://www.omdbapi.com/",
    "TMDB_API_KEY": os.getenv("TMDB_API_KEY"),
    "TMDB_API_URL": "https://api.themoviedb.org/3",
}
