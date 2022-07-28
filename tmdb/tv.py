from .tmdb import Tmdb
# from datetime import datetime


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

    def populars(self):
        # rslt_json = self.__call("/movie/popular", "")
        # return rslt_json
        return self._call(self._urls["popular"], "")

    # def details(self, movie_id):
    #     rslt_json = self.__call(
    #         f"/movie/{movie_id}",
    #         'videos,trailers,images,casts,translations,keywords,release_dates'
    #         )
    #     rslt_json['genres'] = [i['name'] for i in rslt_json['genres']]
    #     for i in rslt_json['release_dates']['results']:
    #         if i['iso_3166_1'] in self.language:
    #             for d in i['release_dates']:
    #                 d['release_date'][:-1] = datetime.fromisoformat(
    #                     d['release_date'][:-1]
    #                     )
    #                 rslt_json['release_date'] = datetime.fromisoformat(
    #                     rslt_json['release_date']
    #                     )
    #                 if d['release_date'][:-1] == rslt_json['release_date']:
    #                     rslt_json['certification'] = d['certification']
    #     return rslt_json
