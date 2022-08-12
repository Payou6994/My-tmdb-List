from .tmdb import Tmdb


class TV(Tmdb):
    _urls = {
        "details": "/tv/%s",
        "latest": "/tv/latest",
        "search_tv": "/search/tv",
        "popular": "/tv/popular",
        "top_rated": "/tv/top_rated",
        "similar": "/tv/%s/similar",
        "recommendations": "/tv/%s/recommendations",
        "videos": "/tv/%s/videos",
        "airing_today": "/tv/airing_today",
        "on_the_air": "/tv/on_the_air",
        "screened_theatrically": "/tv/%s/screened_theatrically",
        "external_ids": "/tv/%s/external_ids",
        "reviews": "/tv/%s/reviews",
        "keywords": "/tv/%s/keywords",
        "watch_providers": "/tv/%s/watch/providers",
    }

    def populars(self: object):
        return self._call(self._urls["popular"], "")
