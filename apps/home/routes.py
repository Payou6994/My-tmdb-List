from io import BytesIO

import requests
from flask import redirect, render_template, request, send_file, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from flask_login import current_user

from apps import db
from apps.home import blueprint
from apps.home.util import creditHelpers
from apps.home.models import Watchlist, Watched
from tmdb import movies, search, tmdb, trendings, tv

# from dotenv import load_dotenv

# load_dotenv()
tmdb = tmdb.Tmdb()
movies = movies.Movies()
tvs = tv.TV()
trendings = trendings.Trendings()
search = search.Search()


@blueprint.route("/image/<path:path>/<image_id>")
@login_required
def image_proxy(path, image_id):
    if image_id != "None":
        url = "https://image.tmdb.org/%s/%s" % (path, image_id)
        rslt = requests.get(url)
        buffer_image = BytesIO(rslt.content)
        buffer_image.seek(0)
        return send_file(buffer_image, mimetype="image/jpeg")
    else:
        return send_file("./static/assets/img/no_image.jpg", mimetype="image/jpeg")


@blueprint.route("/index")
@login_required
def index():
    populars_movies = movies.populars()
    populars_tvs = tvs.populars()
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


@blueprint.route("/movie/<movie_id>", methods=["GET", "POST"])
@login_required
def movie_details(movie_id: int):
    watched = Watched.query.filter_by(userId=current_user.id, tmdbId=movie_id).first()
    watchlist = Watchlist.query.filter_by(
        userId=current_user.id, tmdbId=movie_id
    ).first()

    if request.method == "POST":
        try:
            if request.form["watched_btn"]:
                if not watched:
                    watched = Watched(**{"userId": current_user.id, "tmdbId": movie_id})
                    db.session.add(watched)
                elif watched:
                    db.session.delete(watched)
                    watched = None
        except:
            pass

        try:
            if request.form["watchlist_btn"]:
                if not watchlist:
                    watchlist = Watchlist(
                        **{"userId": current_user.id, "tmdbId": movie_id}
                    )
                    db.session.add(watchlist)
                elif watchlist:
                    db.session.delete(watchlist)
                    watchlist = None
        except:
            pass

        db.session.commit()

    entity = movies.details(movie_id)
    entity["credits"]["crew"] = creditHelpers(entity["credits"]["crew"])
    return render_template(
        "home/movie.html", entity=entity, watched=watched, watchlist=watchlist
    )


@blueprint.route("/tv/<id>")
@login_required
def tv_details(id: int):
    entity = tvs.details(id)
    for i in range(len(entity["credits"]["crew"])):
        if i >= len(entity["created_by"]):
            break
        entity["credits"]["crew"].append(
            {
                "id": entity["credits"]["crew"][i]["id"],
                "name": entity["credits"]["crew"][i]["name"],
                "job": "Creator",
            }
        )
    entity["credits"]["crew"] = creditHelpers(entity["credits"]["crew"])
    return render_template("home/tv.html", entity=entity)


@blueprint.route("/search", methods=["GET", "POST"])
@login_required
def post_search():
    if request.method == "POST":
        search_word = request.form.get("search")
        return redirect(url_for("home_blueprint.post_search", query=search_word))
    else:
        search_word = request.args.get("query")
        entities = search.multi(search_word)
        return (
            render_template(
                "home/list.html",
                entities=entities,
                search_word=search_word,
                title="Résultats de la recherche",
                segment="search",
            ),
            "Search",
        )


@blueprint.route(
    "/discover/<query>",
)
@login_required
def discover_list(query):
    max = 5
    if query == "trendings":
        entities = trendings.all_day()
        [entities.extend(trendings.all_day(page)) for page in range(2, max)]
    elif query == "movies":
        entities = movies.populars()
        [entities.extend(movies.populars(page)) for page in range(2, max)]
    elif query == "tvs":
        entities = tvs.populars()
        [entities.extend(tvs.populars(page)) for page in range(2, max)]

    return (
        render_template(
            "home/list.html",
            entities=entities,
            title="Tendances",
            segment="trendings",
        ),
        "Trendings",
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
