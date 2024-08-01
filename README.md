
```markdown
# Movie Recommendation Flask API

This project is a Flask web application that utilizes the OMDb API to provide movie recommendations and display movie information. Users can enter a movie title to retrieve relevant details.

## Features

- Allows users to enter a movie title and fetch information from the OMDb API.
- Displays details such as title, year, genre, director, plot, actors, and IMDb rating.

## Technologies

- **Flask**: Python web framework.
- **Requests**: For making HTTP requests.
- **python-dotenv**: For managing environment variables.
- **Tailwind CSS**: For user interface styling.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate     # Windows
   ```

2. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file in the root directory of your project and add your OMDb API key in the following format:

   ```env
   OMDB_API_KEY=your_api_key_here
   ```

4. **Run the Application:**

   ```bash
   flask run
   ```

   Visit `http://127.0.0.1:5000` in your web browser to view the application.

## Usage

1. Open the application in your web browser.
2. Enter a movie title in the "Enter movie title" field.
3. Click the "Search" button.
4. Movie details (title, year, genre, director, plot, actors, IMDb rating) will be displayed on the screen.
