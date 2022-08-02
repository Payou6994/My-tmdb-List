from flask import Flask, render_template
from tmdb import tmdb, movies, tv, trendings


app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"
tmdb = tmdb.Tmdb()
tmdb.api_key = '8455657f72d491d8c72563e88212ce94'
tmdb.language = 'fr-FR'
movies = movies.Movies()
tv = tv.TV()
trendings = trendings.Trendings()


@app.route("/")
def index():
    populars_movies = movies.populars()
    populars_tvs = tv.populars()
    tredings_all_day = trendings.all_day()

    return render_template(
        "index.html",
        popularsMovies=populars_movies,
        popularsTvs=populars_tvs,
        trendings=tredings_all_day
    )


@app.route("/movie/<id>")
def movie_details(movie_id):
    movie = movies.details(movie_id)
    return render_template('movie.html', tables=movie)
