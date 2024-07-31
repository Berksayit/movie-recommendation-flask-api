from flask import Flask, jsonify, request, render_template
import requests
from googletrans import Translator

app = Flask(__name__)

# OMDb API anahtarınızı buraya ekleyin
OMDB_API_KEY = '77ae9d39'
OMDB_API_URL = 'http://www.omdbapi.com/'

# Çeviri için Google Translator kullanımı
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    if not title:
        return render_template('index.html', error="Film adı girilmelidir.")
    
    # OMDb API'ye istek gönder
    try:
        response = requests.get(OMDB_API_URL, params={'t': title, 'apikey': OMDB_API_KEY})
        response.raise_for_status()  # HTTP hata kodlarını yakalamak için
        data = response.json()

        # API yanıtını kontrol et
        if data['Response'] == 'True':
            # Çeviriyi yap
            plot_translation = translator.translate(data.get('Plot'), src='en', dest='tr').text

            # Türleri Türkçeye çevir
            genres = data.get('Genre', '').split(', ')
            genre_translation_text = ', '.join(
                translator.translate(g, src='en', dest='tr').text for g in genres
            )

            movie_info = {
                "Film Adı": data.get('Title'),
                "Yıl": data.get('Year'),
                "Tür": genre_translation_text,
                "Yönetmen": data.get('Director'),
                "Konu": plot_translation,
                "Oyuncular": data.get('Actors'),
                "IMDb Reytingi": data.get('imdbRating')
            }
            return render_template('index.html', movie=movie_info)
        else:
            return render_template('index.html', error=data['Error'])
    except requests.RequestException as e:
        # API isteği sırasında bir hata oluştuysa
        return render_template('index.html', error=f"HTTP Hata: {e}")

if __name__ == '__main__':
    app.run(debug=True)
