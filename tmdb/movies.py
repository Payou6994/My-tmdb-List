from datetime import datetime

from tmdb import Tmdb


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

    def populars(self):
        return self._call(self._urls["popular"], "")

    def details(self, movie_id):
        rslt_json = self._call(
            self._urls["details"] % movie_id,
            "videos,trailers,images,casts,translations,keywords,release_dates",
        )
        for i in rslt_json["release_dates"]:
            if i["iso_3166_1"] in self.language:
                for date in i["release_dates"]:
                    date["release_date"][:-1] = datetime.fromisoformat(
                        date["release_date"][:-1]
                    )
                    rslt_json["release_date"] = datetime.fromisoformat(
                        rslt_json["release_date"]
                    )
                    if date["release_date"][:-1] == rslt_json["release_date"]:
                        rslt_json["certification"] = date["certification"]
        return rslt_json
