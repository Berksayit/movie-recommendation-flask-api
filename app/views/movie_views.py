from flask import Blueprint, request, jsonify, render_template
from ..models.omdb_model import fetch_movie_details

movie_views = Blueprint('movie_views', __name__)

@movie_views.route('/')
def index():
    return render_template('index.html')

@movie_views.route('/api/search', methods=['POST'])
def search_api():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Movie title is required.'}), 400
    
    try:
        movie_info = fetch_movie_details(title)
        return jsonify(movie_info)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except SystemError as e:
        return jsonify({'error': str(e)}), 500
