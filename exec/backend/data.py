import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()
import requests
from movies.models import Movie,Movie_genre_list

# TMDB_KEY = 'd9560dbd976c10837a85763f71ab79b1'
# LANGUAGE = 'ko-KR'

# REGION = 'KR'

# genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={ TMDB_KEY }&language=ko-KR'

# genre_response = requests.get(genre_url).json().get('genres')

# for genre in genre_response:
#     new_genre = Genre()
#     new_genre.id = genre['id']
#     new_genre.name = genre['name']
#     new_genre.save()


import requests
from urllib.parse import urlparse
import json

# V3webSENgNZcxXmFjeWh
# v7Sp8LlYEk
# d9560dbd976c10837a85763f71ab79b1 : Tmdb
# https://api.themoviedb.org/3/movie/3?api_key=d9560dbd976c10837a85763f71ab79b1&language=ko-kr

class URLMaker():
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    key = 'd9560dbd976c10837a85763f71ab79b1'

    def __init__(self,key):
        self.key = key

    def get_url(self,num):
        return f'{self.url}?api_key={self.key}'

#https://api.themoviedb.org/3/movie/now_playing?api_key=d9560dbd976c10837a85763f71ab79b1&language=ko-KR&page=14
def movieInfo():
    url_maker = URLMaker('d9560dbd976c10837a85763f71ab79b1')
    page = 1
    while page < 2 : 
        url = url_maker.get_url(page)
        url_1 = f'{url}&language=ko-kr&{page}'
        movies_dict = requests.get(url_1)
        movie = movies_dict.json()
        print("비비")
        try:
            for i in range(len(movie['results'])):
                print(i)
                m_rst = movie['results'][i]
                print(m_rst)
                if m_rst['overview'] and m_rst['adult'] == False:
                    print("처리2")
                    data = Movie.objects.cre
                    print(m_rst['title'])
                    new_movie = Movie(title=m_rst['title'])
                    print(new_movie)
                    new_movie.title = m_rst['title']
                    print(new_movie)
                    new_movie.original_title = m_rst['original_title']
                    poster_path = m_rst['poster_path']
                    new_movie.poster_path= f'https://image.tmdb.org/t/p/w500/{poster_path}'
                    new_movie.release_date = m_rst['release_date']
                    new_movie.runtime = m_rst['runtime']    
                    new_movie.popularity = m_rst['popularity']
                    new_movie.vote_average = m_rst['vote_average']
                    new_movie.overview = m_rst['overview']
                    print(new_movie)
                    new_movie.save()
                    print("처리33")
                    for genre in m_rst['genres']:
                        new_movie.genres.add(genre['id'])
                    
                    print("처리")
                



        except:
            pass
        page += 1

if __name__== '__main__':
    print("dd")
    movieInfo()
