# app.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database setup
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        year INTEGER
    )
''')
conn.commit()
conn.close()

# Model for Movie
class Movie:
    def __init__(self, id, title, genre, year):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year

# Adding movies
movies_data = [
    {"title": "Godfather", "genre": "Crime", "year": 1972},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},
    {"title": "Gone Girl", "genre": "Mystery", "year": 2014},
    {"title": "Wonka", "genre": "Fantasy", "year": 1971},
]

for movie_data in movies_data:
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)', (movie_data['title'], movie_data['genre'], movie_data['year']))
    conn.commit()
    conn.close()

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    movies_data = cursor.fetchall()
    conn.close()

    movies = [Movie(*movie_data) for movie_data in movies_data]
    movies_json = [{"id": movie.id, "title": movie.title, "genre": movie.genre, "year": movie.year} for movie in movies]

    return jsonify(movies_json)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)', (data['title'], data['genre'], data['year']))
    conn.commit()
    conn.close()

    return jsonify({"message": "Movie added successfully"})

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.json
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE movies SET title=?, genre=?, year=? WHERE id=?', (data['title'], data['genre'], data['year'], movie_id))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Movie with ID {movie_id} updated successfully"})

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM movies WHERE id=?', (movie_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Movie with ID {movie_id} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

