from flask import Flask, render_template, request

# from flask_caching import Cache, CachedResponse
from tmdbapi import tmdb
import random

# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb()


@app.route("/")
def index():
    popularsMovies = tmdb.popular_movies()
    popularsTvs = tmdb.popular_tv()
    trendingMovies = tmdb.trending("all", "day")

    return render_template(
        "index.html",
        popularsMovies=popularsMovies,
        popularsTvs=popularsTvs,
        trendings=trendingMovies,
    )


@app.route("/movie/<id>")
def movie(id):
    movie = tmdb.movie(id)
    return render_template("movie.html", movie=movie)


@app.route("/tv/<id>")
def tv(id):
    tv = tmdb.tv(id)
    return render_template("tv.html", tv=tv)
