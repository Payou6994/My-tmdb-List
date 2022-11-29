from .tmdb import Tmdb
from .exceptions import TMDbException


class Movies(Tmdb):
    _urls = {
        "details": "/movie/%s",
        "alternative_titles": "/movie/%s/alternative_titles",
        "changes": "/movie/%s/changes",
        "credits": "/movie/%s/credits",
        "external_ids": "/movie/%s/external_ids",
        "images": "/movie/%s/images",
        "keywords": "/movie/%s/keywords",
        "lists": "/movie/%s/lists",
        "reviews": "/movie/%s/reviews",
        "videos": "/movie/%s/videos",
        "recommendations": "/movie/%s/recommendations",
        "latest": "/movie/latest",
        "now_playing": "/movie/now_playing",
        "top_rated": "/movie/top_rated",
        "upcoming": "/movie/upcoming",
        "popular": "/movie/popular",
        "search_movie": "/search/movie",
        "similar": "/movie/%s/similar",
        "external": "/find/%s",
        "release_dates": "/movie/%s/release_dates",
        "watch_providers": "/movie/%s/watch/providers",
    }

    def details(self: object, movie_id: int):
        return self._call(
            self._urls["details"] % movie_id,
            "videos,trailers,images,casts,translations,keywords,release_dates",
        )

    def recommendations(self: object, movie_id: int):
        return self._call(
            self._urls["recommendations"] % movie_id,
            "",
        )

    def populars(self: object):
        return self._call(self._urls["popular"], "")

    def similar(self: object, movie_id: int):
        return self._call(
            self._urls["similar"] % movie_id,
            "",
        )

    def watch_providers(self: object, movie_id: int):
        return self._call(self._urls["watch_providers"] % movie_id)
