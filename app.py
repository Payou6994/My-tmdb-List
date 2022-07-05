from flask import Flask, render_template, request
from tmdbapi import tmdb
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb()


@app.route("/", methods=["GET", "POST"])
def index():
    popularsMovie = tmdb.popular_movies()
    popularsTv = tmdb.popular_tv()

    if request.method == "POST":
        if request.form.get("trending_day") == "Aujourd'hui":
            trendingMovies = tmdb.trending("all", "day")
        elif request.form.get("trending_week") == "Cette semaine":
            trendingMovies = tmdb.trending("all", "week")
        else:
            trendingMovies = tmdb.trending("all", "day")
    elif request.method == "GET":
        trendingMovies = tmdb.trending("all", "day")

    populars = popularsMovie + popularsTv
    random.shuffle(populars)

    for i in range(len(populars)):
        populars[i]["vote_average"] = round(populars[i]["vote_average"])

    for i in range(len(trendingMovies)):
        trendingMovies[i]["vote_average"] = round(trendingMovies[i]["vote_average"])

    return render_template("index.html", populars=populars, trendings=trendingMovies)
