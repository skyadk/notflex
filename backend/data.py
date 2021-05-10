import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

import requests
from movie.models import Genre, Movie

TMDB_KEY = 'd9560dbd976c10837a85763f71ab79b1'
LANGUAGE = 'ko-KR'

REGION = 'KR'

genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={ TMDB_KEY }&language=ko-KR'

genre_response = requests.get(genre_url).json().get('genres')

for genre in genre_response:
    new_genre = Genre()
    new_genre.id = genre['id']
    new_genre.name = genre['name']
    new_genre.save()


import requests
from urllib.parse import urlparse
import json

# V3webSENgNZcxXmFjeWh
# v7Sp8LlYEk
# d9560dbd976c10837a85763f71ab79b1 : Tmdb
# https://api.themoviedb.org/3/movie/3?api_key=d9560dbd976c10837a85763f71ab79b1&language=ko-kr

class URLMaker():
    url = 'https://api.themoviedb.org/3/movie/'
    key = 'd9560dbd976c10837a85763f71ab79b1'

    def __init__(self,key):
        self.key = key

    def get_url(self,num):
        return f'{self.url}{num}?api_key={self.key}'


def movieInfo():
    url_maker = URLMaker('d9560dbd976c10837a85763f71ab79b1')
    i = 100
    while i < 300 : 
        url = url_maker.get_url(i)
        url_1 = f'{url}&language=ko-kr'
        movies_dict = requests.get(url_1)
        movie = movies_dict.json()
        try:
            if movie['overview'] and movie['adult'] == False:
                new_movie = Movie()
                new_movie.title = movie['title']
                new_movie.original_title = movie['original_title']
                poster_path = movie['poster_path']
                new_movie.poster_path= f'https://image.tmdb.org/t/p/w500/{poster_path}'
                new_movie.release_date = movie['release_date']
                new_movie.runtime = movie['runtime']    
                new_movie.popularity = movie['popularity']
                new_movie.vote_average = movie['vote_average']
                new_movie.overview = movie['overview']
                
                new_movie.save()
                
                for genre in movie['genres']:
                    new_movie.genres.add(genre['id'])
                



        except:
            pass
        i += 1

if __name__=='__main__':
    movieInfo()
