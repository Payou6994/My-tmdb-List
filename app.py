from re import I
from flask import Flask, render_template
from tmdbapi import tmdb
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb()


@app.route("/")
def index():
    popularsMovie = tmdb.popular_movies()
    popularsTv = tmdb.popular_tv()
    trendingMovies = tmdb.trending("all", "week")

    populars = popularsMovie + popularsTv
    random.shuffle(populars)

    return render_template("index.html", populars=populars, trendings=trendingMovies)
