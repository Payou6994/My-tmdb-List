import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import tmdb_requests as tmdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    popularMovies = tmdb.popular_movie()
    return render_template('index.html', movies=popularMovies)

@app.route('/movies')
def movies():
    movies = tmdb.popular_movie()
    return render_template('movies.html', movies=movies)

@app.route('/movie/<id>')
def details_movies(id):
    movies = tmdb.details_movie(id)
    return render_template('movie.html', movies=movies)

@app.route('/tv')
def tv():
    tv = tmdb.popular_tv()
    return render_template('tv.html', tv=tv)