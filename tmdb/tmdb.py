import os
import requests
from .exceptions import TMDbException


class Tmdb:
    TMDB_API_KEY = "TMDB_API_KEY"
    TMDB_LANGUAGE = "TMDB_LANGUAGE"
    # DATE_FORMAT = "DATE_FORMAT"
    FROM_JSON = "FROM_JSON"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"
        if os.environ.get(self.TMDB_LANGUAGE) is None:
            os.environ[self.TMDB_LANGUAGE] = "en-US"

        # if os.environ.get(self.DATE_FORMAT) is None:
        #     os.environ[self.DATE_FORMAT] = "%Y-%m-%d"

    @property
    def api_key(self: object):
        return os.environ.get(self.TMDB_API_KEY)

    @api_key.setter
    def api_key(self: object, api_key: str):
        os.environ[self.TMDB_API_KEY] = str(api_key)

    @property
    def language(self: object):
        return os.environ.get(self.TMDB_LANGUAGE)

    @language.setter
    def language(self: object, language: str):
        os.environ[self.TMDB_LANGUAGE] = language

    # @property
    # def date_format(self: object):
    #     return os.environ.get(self.DATE_FORMAT)

    # @date_format.setter
    # def date_format(self: object, format: str):
    #     os.environ[self.DATE_FORMAT] = format

    @property
    def from_json(self: object):
        return os.environ.get(self.FROM_JSON)

    @from_json.setter
    def from_json(self: object, from_json: str):
        os.environ[self.FROM_JSON] = from_json

    def _call(self: object, action: str, append_to_response=""):
        if self.api_key is None or self.api_key == "":
            raise TMDbException("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s" % (
            self._base,
            action,
            self.api_key,
            append_to_response,
            self.language,
        )

        rslt_json = requests.get(url).json()

        if "success" in rslt_json and rslt_json["success"] is False:
            raise TMDbException(rslt_json["status_message"])

        if "results" in rslt_json:
            rslt_json = rslt_json["results"]

        return rslt_json
