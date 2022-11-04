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

    def populars(self: object):
        result = self._call(self._urls["popular"], "")
        return result

    def details(self: object, movie_id: int):
        result = self._call(
            self._urls["details"] % movie_id,
            "videos,trailers,images,casts,translations,keywords,release_dates",
        )
        return result
