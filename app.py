from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# OMDb API key
OMDB_API_KEY = '77ae9d39'
OMDB_API_URL = 'http://www.omdbapi.com/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    if not title:
        return render_template('index.html', error="Movie title is required.")
    
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
            return render_template('index.html', movie=movie_info)
        else:
            return render_template('index.html', error=data['Error'])
    except requests.RequestException as e:
        # Handle HTTP request errors
        return render_template('index.html', error=f"HTTP Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)