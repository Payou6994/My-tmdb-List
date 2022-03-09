from flask import Flask, render_template
from datetime import datetime
import tmdb_requests as tmdb

app = Flask(__name__)
app.config["SECRET_KEY"] = "your secret key"


@app.route("/")
def index():
    popularMovies = tmdb.popular_movie()
    popularTvs = tmdb.popular_tv()
    for ob in popularTvs:
        date = ob.first_air_date
        ob.first_air_date = datetime.strptime(date,'%Y-%m-%d')
        print(date.strftime("%d %b, %Y"))

    return render_template("index.html", movies=popularMovies, tvs=popularTvs)