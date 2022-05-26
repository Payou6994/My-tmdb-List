import requests
class tmdb(object):
    api_key = "8455657f72d491d8c72563e88212ce94"
    language = "fr_FR"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"

    def _call(self, action):
        url = "%s%s?api_key=%s&language=%s" % (
            self._base,
            action,
            self.api_key,
            self.language,
        )
        result = requests.get(url)
        return result

    def popular_movies(self):
        result = self._call("/movie/popular")
        rslt_json = result.json()['results']
        return rslt_json

    def popular_tvs(self):
        result = self._call("/tv/popular")
        rslt_json = result.json()['results']
        return rslt_json
