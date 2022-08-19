from flask import Flask, render_template
from tmdb import tmdb, movies, tv, trendings
from db_request import get_data

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb.Tmdb()
tmdb.api_key = "8455657f72d491d8c72563e88212ce94"
tmdb.language = "fr-FR"
tmdb.date_format = "%d/%m/%Y"
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
    data = get_data("movies_items", movie_id)
    if data:
        movie = data
    else:
        movie = movies.details(movie_id)
    return render_template("movie-dev.html", entity=movie, date_format=tmdb.date_format)
