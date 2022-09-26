from flask import Flask, render_template
from tmdb import tmdb, movies, tv, trendings
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
tmdb = tmdb.Tmdb()
tmdb.api_key = os.getenv("API_KEY")
tmdb.language = os.getenv("LANGUAGE")
tmdb.date_format = os.getenv("DATE_FORMAT")

movies = movies.Movies()
tv = tv.TV()
trendings = trendings.Trendings()


@app.route("/")
def index():
    populars_movies = movies.populars()
    populars_tvs = tv.populars()
    trendings_all_day = trendings.all_day()

    return render_template(
        "index.html",
        popularsMovies=populars_movies,
        popularsTvs=populars_tvs,
        trendings=trendings_all_day,
    )


@app.route("/movie/<movie_id>")
def movie_details(movie_id: int):
    movie = movies.details(movie_id)
    return render_template(
        "movie-dev.html",
        entity=movie,
        casts=movie["casts"]["cast"],
        date_format=tmdb.date_format,
    )
