from flask import Flask, render_template
from tmdb import tmdb, movies, tv, trendings
# from tmdb import movies

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
    popularsMovies = movies.populars()
    popularsTvs = tv.populars()
    trendingAllDay = trendings.all_day()

    return render_template(
        "index.html",
        popularsMovies=popularsMovies,
        popularsTvs=popularsTvs,
        trendings=trendingAllDay
    )


@app.route("/movie/<id>")
def movie(id):
    movie = movies.details(id)
    return render_template('movie.html', tables=movie)
