
---

# Movie Search Web Application

A simple movie search web application built with Flask. This application allows users to search for movies by title and view detailed information including the plot, director, cast, and IMDb rating. Users can also view a list of the top 20 movies based on ratings and the most searched movie of the day.

## Features

- **Search for Movies**: Enter a movie title to retrieve detailed information from the OMDb API, including the plot, director, actors, and IMDb rating.
- **Top 20 Movies**: Fetch and display a list of the top 20 movies based on ratings from the TMDb API.
- **Most Searched Movie Today**: View the most searched movie of the day, which is determined by the application and stored in the database.
- **User Authentication**: Register and log in to access personalized features and session management.
- **Unique User Constraints**: Ensure unique usernames and emails for user registration.

## Technologies Used

- **Flask**: A micro web framework for Python used to build the web application.
- **OMDb API**: Provides movie data based on title search.
- **TMDb API**: Provides top-rated movies data.
- **Tailwind CSS**: For styling the web application.
- **SQLAlchemy**: For database management with SQLite.
- **Werkzeug**: For secure password hashing.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/berksayit/movie-search-app.git
    cd movie-search-app
    ```

2. **Set Up a Virtual Environment**:

    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env File**: Create a `.env` file in the project root and add your API keys:

    ```env
    OMDB_API_KEY=your_omdb_api_key
    TMDB_API_KEY=your_tmdb_api_key
    ```

5. **Run the Application**:

    ```bash
    python app.py
    ```

6. **Access the Application**: Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application in action.

## Configuration

- **config.py**: Contains configuration settings for the application.
  - `OMDB_API_KEY`: Your OMDb API key.
  - `OMDB_API_URL`: Base URL for the OMDb API.
  - `TMDB_API_KEY`: Your TMDb API key.
  - `TMDB_API_URL`: Base URL for the TMDb API.

## API Endpoints

- **GET /**: Home page with the search form and buttons for displaying top 20 movies and the most searched movie today.
- **POST /api/search**: Searches for a movie by title using the OMDb API.
  - **Request Body**: `{ "title": "movie title" }`
  - **Response**: JSON object with movie details or error message.
- **GET /api/top20**: Retrieves the top 20 movies based on ratings from the TMDb API.
  - **Response**: JSON array of movie objects with title, release date, rating, overview, and poster URL.
- **GET /api/most_searched_today**: Retrieves the most searched movie of the day from the database.
  - **Response**: JSON object with movie details or error message.

## Project Structure

- `run.py`: Main application file containing the Flask routes and logic.
- `app/config.py`: Configuration file with API keys and URLs.
- `app/templates/index.html`: HTML template for the front-end interface.
- `app/templates/register.html`: HTML template for user registration.
- `app/templates/login.html`: HTML template for user login.
- `.env`: Environment file for storing API keys.
- `requirements.txt`: Lists the Python packages required for the project.
- `user.db`: SQLite database file for storing user information.
- `search.db`: SQLite database file for storing movie search data.

## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes.

## Acknowledgments

- OMDb API
- TMDb API
- Tailwind CSS

---
