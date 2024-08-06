from flask import Flask, request, render_template, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# OMDb API key from .env file
OMDB_API_KEY = os.getenv('OMDB_API_KEY')
OMDB_API_URL = 'http://www.omdbapi.com/'

# TMDb API key from .env file
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search_api():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Movie title is required.'}), 400
    
    try:
        response = requests.get(OMDB_API_URL, params={'t': title, 'apikey': OMDB_API_KEY})
        response.raise_for_status()
        data = response.json()

        if data['Response'] == 'True':
            movie_info = {
                "Title": data.get('Title'),
                "Year": data.get('Year'),
                "Genre": data.get('Genre'),
                "Director": data.get('Director'),
                "Plot": data.get('Plot'),
                "Actors": data.get('Actors'),
                "IMDb Rating": data.get('imdbRating')
            }
            return jsonify(movie_info)
        else:
            return jsonify({'error': data['Error']}), 400
    except requests.RequestException as e:
        return jsonify({'error': f"HTTP Error: {e}"}), 500

@app.route('/api/top20', methods=['GET'])
def top20_movies():
    try:
        response = requests.get(f'{TMDB_API_URL}/movie/top_rated', params={'api_key': TMDB_API_KEY, 'language': 'en-US', 'page': 1})
        response.raise_for_status()
        data = response.json()
        
        top20 = data['results'][:20]
        
        top20_movies = [{
            'Title': movie['title'],
            'Release Date': movie['release_date'],
            'Rating': movie['vote_average'],
            'Overview': movie['overview'],
            'Poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else 'https://via.placeholder.com/150'
        } for movie in top20]
        
        return jsonify(top20_movies)
    except requests.RequestException as e:
        return jsonify({'error': f"HTTP Error: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
