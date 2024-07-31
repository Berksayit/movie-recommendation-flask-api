

# Movie Recommendation Flask API

## Description

The Movie Recommendation Flask API is a web service that provides movie recommendations to users. Built with Flask, this API allows users to receive suggestions based on various criteria from a movie database. The project is built on Python and the Flask framework.

## Features

- **Movie Recommendations**: Users can receive movie recommendations based on specific criteria.
- **RESTful API**: Provides and retrieves data through HTTP requests.
- **Simple and Quick Setup**: Easily set up with a minimal Flask-based structure.

## Getting Started

### Requirements

- Python 3.7 or higher
- Flask
- Flask-RESTful
- Other necessary Python packages

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/movie-recommendation-flask-api.git
   cd movie-recommendation-flask-api
   ```

2. **Create a Virtual Environment**

   Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   By default, the API will run at `http://127.0.0.1:5000`.

### Usage

You can test your API by making various HTTP requests. Here are a few examples:

- **Get Movie Recommendations**

  ```bash
  curl -X GET http://127.0.0.1:5000/recommendations?genre=action
  ```

  This request will return recommendations for action genre movies.

## API Reference

- **GET /recommendations**

  - **Parameters**:
    - `genre` (optional): Genre of the movie (e.g., `action`, `comedy`)
    - `rating` (optional): Movie rating (e.g., `7`, `8`)

  - **Response**:
    ```json
    {
      "recommendations": [
        {
          "title": "Movie Title",
          "genre": "Movie Genre",
          "rating": "Movie Rating"
        },
        ...
      ]
    }
    ```

