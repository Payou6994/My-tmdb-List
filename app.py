from flask import Flask, render_template, request
import pandas as pd
# from flask_caching import Cache, CachedResponse
# from tmdbapi import tmdb
from tmdbapiV2 import TMDb,Movie
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = TMDb()
tmdb.api_key = '8455657f72d491d8c72563e88212ce94'
tmdb.language = 'fr'
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


@app.route("/movie/<iid>")
def movie(iid):
    movie = Movie()
    movie = movie.details(iid)
    # movie = tmdb.movie.details(iid)
    return render_template("txt.html", movie=movie)

@app.route("/movie-dev/<iid>")
def movie_dev(iid):
    movie = tmdb.movie(iid)
    df = pd.DataFrame.from_dict(movie,orient='index')
    return render_template('movie-dev.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route("/tv/<iid>")
def tv(iid):
    tv = tmdb.tv(iid)
    return render_template("tv.html", tv=tv)