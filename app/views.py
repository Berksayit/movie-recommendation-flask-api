from . import app, Config
from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import requests
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.permanent_session_lifetime = timedelta(minutes=15)  # Set session lifetime to 15 minutes

# SQLAlchemy setup
DATABASE_URL = 'sqlite:///users.db'
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Initialize database
def init_db():
    Base.metadata.create_all(engine)

init_db()

def is_logged_in():
    return 'username' in session

@app.route('/')
def index():
    if not is_logged_in():
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        
        db_session = SessionLocal()
        
        existing_user = db_session.query(User).filter((User.username == username) | (User.email == email)).all()
        if existing_user:
            username_error = ''
            email_error = ''
            if any(user.username == username for user in existing_user):
                username_error = 'Username is already taken.'
            if any(user.email == email for user in existing_user):
                email_error = 'Email is already used.'
                
            db_session.close()
            return render_template('register.html', username_error=username_error, email_error=email_error)
        
        try:
            new_user = User(username=username, password=hashed_password, email=email)
            db_session.add(new_user)
            db_session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db_session.rollback()
            return 'An error occurred: ' + str(e)
        finally:
            db_session.close()
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']  # Username or email
        password = request.form['password']
        
        db_session = SessionLocal()
        
        user = db_session.query(User).filter((User.username == identifier) | (User.email == identifier)).first()
        
        if user is None:
            db_session.close()
            flash('Invalid username or email!', 'error')
            return redirect(url_for('login'))
        
        if check_password_hash(user.password, password):
            session.permanent = True
            session['username'] = user.username
            db_session.close()
            return redirect(url_for('index'))
        else:
            db_session.close()
            flash('Invalid password!', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/api/search', methods=['POST'])
def search_api():
    if not is_logged_in():
        return jsonify({'error': 'Unauthorized'}), 401

    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Movie title is required.'}), 400
    
    try:
        response = requests.get(Config["OMDB_API_URL"], params={'t': title, 'apikey': Config["OMDB_API_KEY"]})
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
    if not is_logged_in():
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        response = requests.get(f'{Config["TMDB_API_URL"]}/movie/top_rated', params={'api_key': Config["TMDB_API_KEY"], 'language': 'en-US', 'page': 1})
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
