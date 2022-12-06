import os
import requests
from .exceptions import TMDbException
from flask_login import current_user

class Tmdb:
    TMDB_API_KEY = "TMDB_API_KEY"
    # TMDB_LANGUAGE = "TMDB_LANGUAGE"
    # TMDB_REGION = "TMDB_REGION"

    def __init__(self):
        self._base = "https://api.themoviedb.org/3"
        # if os.environ.get(self.TMDB_LANGUAGE) is None:
        #     os.environ[self.TMDB_LANGUAGE] = "en-US"
        if os.environ.get(self.TMDB_API_KEY) is None:
            os.environ[self.TMDB_API_KEY] = "8455657f72d491d8c72563e88212ce94"
    @property
    def api_key(self: object):
        return os.environ.get(self.TMDB_API_KEY)

    @api_key.setter
    def api_key(self: object, api_key: str):
        os.environ[self.TMDB_API_KEY] = str(api_key)

    # @property
    # def language(self: object):
    #     return os.environ.get(self.TMDB_LANGUAGE)

    # @language.setter
    # def language(self: object, language: str):
    #     os.environ[self.TMDB_LANGUAGE] = language

    # @property
    # def region(self: object):
    #     return os.environ.get(self.TMDB_REGION)

    # @region.setter
    # def region(self: object, region: str):
    #     os.environ[self.TMDB_REGION] = region

    def _call(self: object, action: str, append_to_response):
        if self.api_key is None or self.api_key == "":
            raise TMDbException("No API key found.")

        url = "%s%s?api_key=%s&%s&language=%s&region=%s" % (
            self._base,
            action,
            self.api_key,
            append_to_response,
            current_user.language,
            current_user.region,
        )

        rslt_json = requests.get(url).json()

        if "success" in rslt_json and rslt_json["success"] is False:
            raise TMDbException(rslt_json["status_message"])

        if "results" in rslt_json:
            rslt_json = rslt_json["results"]

        return rslt_json

    def _type(self: object, result: list, type: str):
        for i in result:
            i["media_type"] = type
        return result
