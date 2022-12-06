from .tmdb import Tmdb


class Trendings(Tmdb):
    _urls = {
        "all_day": "/trending/all/day",
        "all_week": "/trending/all/week",
        "movie_day": "/trending/movie/day",
        "movie_week": "/trending/movie/week",
        "tv_day": "/trending/tv/day",
        "tv_week": "/trending/tv/week",
        "person_day": "/trending/person/day",
        "person_week": "/trending/person/week",
    }

    def all_day(self: object, page=1):
        """
        Get all daily trending
        :param page: int
        :return:
        """
        return self._call(self._urls["all_day"], "page={}".format(page))

    def all_week(self: object):
        """
        Get all weekly trending
        :param page: int
        :return:
        """
        return self._call(self._urls["all_week"], "")
