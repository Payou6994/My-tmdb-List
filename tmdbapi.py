import requests


class tmdb(object):
    api_key = "8455657f72d491d8c72563e88212ce94"
    language = "fr-FR"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"

    def _call(self, action):
        url = f"{self._base}{action}?api_key={self.api_key}&language={self.language}"
        result = requests.get(url)
        try:
            rslt_json = result.json()["results"]
        except KeyError:
            rslt_json = result.json()
        return rslt_json

    def _get_image():
        pass

    def popular_movies(self):
        rslt_json = self._call("/movie/popular")
        return rslt_json

    def popular_tv(self):
        rslt_json = self._call("/tv/popular")
        return rslt_json

    def trending(self, media_type, time_window):
        rslt_json = self._call(f"/trending/{media_type}/{time_window}")
        return rslt_json

    def movie(self, movie_id):
        rslt_json = self._call(f"/movie/{movie_id}")
        print(rslt_json)
        return rslt_json

    def tv(self, tv_id):
        rslt_json = self._call(f"/tv/{tv_id}")
        return rslt_json
