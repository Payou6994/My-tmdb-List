from tmdbv3api import TMDb,Movie,TV
from collections import Counter

tmdb = TMDb()
tmdb.api_key = '8455657f72d491d8c72563e88212ce94'
tmdb.language = 'fr'
tmdb.debug = True

def popular_movie():
    movies = Movie()
    movies = movies.popular()
    return movies

def details_movie(id):
    movies = Movie()
    movies = movies.details(id)
    movies.vote_average = int(movies.vote_average*10)
    for i in range(len(movies.release_dates.results)):
        print(i)
        if movies.release_dates.results[i].iso_3166_1 =='FR':
            movies.certification = movies.release_dates.results[i].release_dates[0].certification
            break
    return movies
    
def popular_tv():
    tv = TV()
    tv = tv.popular()
    tv = [ob.__dict__ for ob in tv]
    return tv
