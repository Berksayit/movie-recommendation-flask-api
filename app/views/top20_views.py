from flask import Blueprint, jsonify
from ..models.tmdb_model import fetch_top20_movies

top20_views = Blueprint('top20_views', __name__)

@top20_views.route('/api/top20', methods=['GET'])
def top20_movies():
    try:
        top20_movies = fetch_top20_movies()
        return jsonify(top20_movies)
    except SystemError as e:
        return jsonify({'error': str(e)}), 500
