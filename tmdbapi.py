from unicodedata import name
import requests
from datetime import datetime
from datetime import timezone


class tmdb(object):
    api_key = "8455657f72d491d8c72563e88212ce94"
    language = "fr-FR"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"
        self.movie = self.movie()

    def __call(self, action, append_to_response):
        if append_to_response:
            url = f"{self._base}{action}?api_key={self.api_key}&language={self.language}&append_to_response={append_to_response}"
        else:
            url = (
                f"{self._base}{action}?api_key={self.api_key}&language={self.language}"
            )
        result = requests.get(url)
        try:
            rslt_json = result.json()["results"]
        except KeyError:
            rslt_json = result.json()
        return rslt_json

    def __get_image():
        pass
    
    def popular_movies(self):
        rslt_json = self.__call("/movie/popular", "")
        return rslt_json

    def popular_tv(self):
        rslt_json = self.__call("/tv/popular", "")
        return rslt_json

    def trending(self, media_type, time_window):
        rslt_json = self.__call(f"/trending/{media_type}/{time_window}", "")
        return rslt_json

    def movie(self, movie_id):
        rslt_json = self.__call(f"/movie/{movie_id}",'videos,trailers,images,casts,translations,keywords,release_dates')
        rslt_json['genres']=[i['name'] for i in rslt_json['genres']]
        for i in rslt_json['release_dates']['results']:
            if i['iso_3166_1'] in self.language:
                for d in i['release_dates']:
                    if datetime.fromisoformat(d['release_date'][:-1]) == datetime.fromisoformat(rslt_json['release_date']):
                        rslt_json['certification'] = d['certification']
        return rslt_json

    def tv(self, tv_id):
        rslt_json = self.__call(
            f"/tv/{tv_id}",
            "videos,trailers,images,casts,translations,keywords,release_dates",
        )
        return rslt_json
