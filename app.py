from flask import Flask, render_template
from tmdbapi import tmdb
app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb()
@app.route("/")
def index():
    popularMovies = tmdb.popular_movies()
    popularTvs = tmdb.popular_tvs()
    return render_template("index.html", movies=popularMovies, tvs=popularTvs)