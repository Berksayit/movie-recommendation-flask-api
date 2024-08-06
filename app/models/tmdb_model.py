import requests
from flask import current_app as app

def fetch_top20_movies():
    try:
        response = requests.get(f"{app.config['TMDB_API_URL']}/movie/top_rated", params={'api_key': app.config['TMDB_API_KEY'], 'language': 'en-US', 'page': 1})
        response.raise_for_status()
        data = response.json()
        
        top20 = data['results'][:20]
        
        return [{
            'Title': movie['title'],
            'Release Date': movie['release_date'],
            'Rating': movie['vote_average'],
            'Overview': movie['overview'],
            'Poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else 'https://via.placeholder.com/150'
        } for movie in top20]
    except requests.RequestException as e:
        raise SystemError(f"HTTP Error: {e}")
