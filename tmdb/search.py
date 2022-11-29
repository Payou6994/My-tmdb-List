from .tmdb import Tmdb
from .exceptions import TMDbException

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Search(Tmdb):
    _urls = {
        "companies": "/search/company",
        "collections": "/search/collection",
        "keywords": "/search/keyword",
        "movies": "/search/movie",
        "multi": "/search/multi",
        "people": "/search/person",
        "tv_shows": "/search/tv",
    }

    def multi(self, params):
        """
        Search for movies.
        :param params:
        :return:
        """
        return self._call(self._urls["multi"], urlencode({"query": params}))