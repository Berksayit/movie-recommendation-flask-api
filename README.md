
---

# Movie Search App

A simple movie search web application built with Flask, which utilizes OMDb and TMDb APIs to fetch and display movie information. Users can search for a movie by title and view details such as the movie's plot, director, cast, and IMDb rating. Additionally, users can view a list of the top 20 movies based on ratings.

## Features

- **Search for Movies**: Enter a movie title to retrieve detailed information from the OMDb API, including the plot, director, actors, and IMDb rating.
- **Top 20 Movies**: Fetch and display a list of the top 20 movies based on ratings from the TMDb API.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **OMDb API**: Provides movie data based on title search.
- **TMDb API**: Provides top-rated movies data.
- **Tailwind CSS**: For styling the web application.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/movie-search-app.git
    cd movie-search-app
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the project root and add your API keys:
    ```env
    OMDB_API_KEY=your_omdb_api_key
    TMDB_API_KEY=your_tmdb_api_key
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Open your browser** and go to `http://127.0.0.1:5000/` to see the application in action.

## API Endpoints

- **GET /**: Home page with the search form and buttons for displaying top 20 movies.
- **POST /api/search**: Searches for a movie by title using the OMDb API.
  - **Request Body**: `{ "title": "movie title" }`
  - **Response**: JSON object with movie details or error message.
- **GET /api/top20**: Retrieves the top 20 movies based on ratings from the TMDb API.
  - **Response**: JSON array of movie objects with title, release date, rating, overview, and poster URL.

## Project Structure

- **app.py**: Main application file containing the Flask routes and logic.
- **templates/index.html**: HTML template for the front-end interface.
- **.env**: Environment file for storing API keys.


## Contributing

Feel free to open issues or submit pull requests for improvements and bug fixes. 

## Acknowledgments

- [OMDb API](http://www.omdbapi.com/)
- [TMDb API](https://www.themoviedb.org/documentation/api)
- [Tailwind CSS](https://tailwindcss.com/)

---
