from flask import Flask, request, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# OMDb API key
OMDB_API_KEY = os.getenv('OMDB_API_KEY')
OMDB_API_URL = 'http://www.omdbapi.com/'

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/search', methods=['POST'])
def search_api():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Movie title is required.'}), 400
    
    # Send request to OMDb API
    try:
        response = requests.get(OMDB_API_URL, params={'t': title, 'apikey': OMDB_API_KEY})
        response.raise_for_status()  # Capture HTTP error codes
        data = response.json()

        # Check the API response
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
        # Handle HTTP request errors
        return jsonify({'error': f"HTTP Error: {e}"}),500

if __name__ == '__main__':
    app.run(debug=True) 
