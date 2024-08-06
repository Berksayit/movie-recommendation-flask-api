import requests
from flask import current_app as app

def fetch_movie_details(title):
    try:
        response = requests.get(app.config['OMDB_API_URL'], params={'t': title, 'apikey': app.config['OMDB_API_KEY']})
        response.raise_for_status()
        data = response.json()
        
        if data['Response'] == 'True':
            return {
                "Title": data.get('Title'),
                "Year": data.get('Year'),
                "Genre": data.get('Genre'),
                "Director": data.get('Director'),
                "Plot": data.get('Plot'),
                "Actors": data.get('Actors'),
                "IMDb Rating": data.get('imdbRating')
            }
        else:
            raise ValueError(data['Error'])
    except requests.RequestException as e:
        raise SystemError(f"HTTP Error: {e}")
    except ValueError as e:
        raise ValueError(f"API Error: {e}")
