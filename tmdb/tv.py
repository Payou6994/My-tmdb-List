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
        "content_ratings": "/tv/%s/content_ratings",
    }

    def details(
        self: object,
        tv_id: int,
        append_to_response="videos,trailers,images,credits,translations,releases,watch/providers,similar,recommendations,content_ratings",
    ):
        return self._call(
            self._urls["details"] % tv_id,
            "append_to_response=" + append_to_response,
        )

    def populars(self: object, page=1):
        return self._type(
            self._type(
                self._call(self._urls["popular"], "page={}".format(page)), "tv"
            ),
            "tv",
        )

    def similar(self, tv_id, page=1):

        return self._type(
            self._call(
                self._urls["similar"] % str(tv_id), "page=" + str(page)
            ),
            "tv",
        )

    def recommendations(self, tv_id, page=1):
        return self._call(
            self._urls["recommendations"] % tv_id, "page=" + str(page)
        )

    def watch_providers(self, tv_id):
        return self._call(self._urls["watch_providers"] % tv_id, "")

    def content_ratings(self, tv_id):
        return self._call(self._urls["content_ratings"] % str(tv_id), "")
