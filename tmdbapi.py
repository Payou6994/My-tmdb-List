import requests


class tmdb(object):
    api_key = "YOUR_API_KEY"
    language = "fr-FR"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"
    def _call(self, action):
        url = f"{self._base}{action}?api_key={self.api_key}&language={self.language}"
        result = requests.get(url)
        return result

    def popular_movies(self):
        result = self._call("/movie/popular")
        rslt_json = result.json()["results"]
        return rslt_json

    def popular_tv(self):
        result = self._call("/tv/popular")
        rslt_json = result.json()["results"]
        return rslt_json

    def trending(self, media_type, time_window):
        result = self._call(f"/trending/{media_type}/{time_window}")
        rslt_json = result.json()["results"]
        return rslt_json
