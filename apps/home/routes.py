import os
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from tmdb import movies, tmdb, trendings, tv
from dotenv import load_dotenv

load_dotenv()
tmdb = tmdb.Tmdb()
tmdb.api_key = os.getenv("API_KEY")
# tmdb.language = current_user.language + "-" + current_user.country
tmdb.from_json = os.getenv("FROM_JSON")
movies = movies.Movies()
tv = tv.TV()
trendings = trendings.Trendings()


@blueprint.route("/index")
@login_required
def index():
    tmdb.language = current_user.language + "-" + current_user.country
    populars_movies = movies.populars()
    populars_tvs = tv.populars()
    trendings_all_day = trendings.all_day()

    return (
        render_template(
            "home/index.html",
            popularsMovies=populars_movies,
            popularsTvs=populars_tvs,
            trendings=trendings_all_day,
            segment="index",
        ),
        "Index",
    )


@blueprint.route("/movie/<movie_id>")
@login_required
def movie_details(movie_id: int):
    movie = movies.details(movie_id)
    watch_providers = movies.watch_providers(movie_id)
    return render_template(
        "movie.html",
        entity=movie,
        watch_providers=watch_providers,
        date_format=tmdb.date_format,
    )


@blueprint.route("/<template>")
@login_required
def route_template(template):

    try:

        if not template.endswith(".html"):
            template += ".html"

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template("home/404.html"), 404

    except:
        return render_template("home/404.html"), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split("/")[-1]

        if segment == "":
            segment = "index"

        return segment

    except:
        return None
