from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MovieListSerializer,MovieDetailSerializer,MovieSerializer,UserSerializer,GetUserSerializer,GetViewListSerializer,GetUidSerializer
from .models import Movie,User, View,Movie_genre_list,Genre

import json, requests

@api_view(['GET'])
def movie_list(request):

    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def moive_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

#email중복체크
@api_view(['POST'])
def userid_check(request):
    email = request.data.get('email')
    # print(email)
    # movieInfo()
    
    if email == None or User.objects.filter(email=email).exists():
        return Response({'fail'})
    
    return Response({'success'})

#로그인정보
@api_view(['POST'])
def get_user(request):
    user = get_object_or_404(User, email=request.data.get('email'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)

#회원가입
@api_view(['POST'])
def join_user(request):
    try:
        if User.objects.filter(email = request.POST["email"]).exists():
            return JsonResponse({"message" : "EXISTS_ID"}, status=400)
        #num 값 갱신
        #user_email = data["id"]
        #전처리 한번 필요
        
        curr_max_num = User.objects.all().count()
        User.objects.create(
            #num = curr_max_num,
            email = request.POST["email"],
            pw = request.POST["pw"],
            nickname = request.POST["nickname"],
            preferGenre = request.POST["preferGenre"]
        ).save()

        data = {
            'email' : request.POST["email"],
            'pw' : request.POST["pw"],
            'nickname' : request.POST["nickname"],
            'preferGenre' : request.POST["preferGenre"]
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json',status=200)
    except KeyError:
        return JsonResponse({"message" : "JOIN_FAILED"},status=400)

@api_view(['POST'])
def get_user_id(request):
    user = get_object_or_404(get_user_model(), id=request.data.get('id'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)    

#내가 시청한목록
@api_view(['GET'])
def my_view_list(request, uid):
    #user = get_object_or_404(User, pk=user_pk)
    #select * from movies_view where uid = user_id;
    view = View.objects.filter(uid=uid).values()
    serializer = GetViewListSerializer(view, many=True)
    return Response(serializer.data)  

#내 시청목록 추가
@api_view(['POST'])
def add_my_view_list(request):
    user_pk = request.data['uid']
    movie_pk = request.data['mid']
    try:
        if movie_exist_check(movie_pk) == False:
            return JsonResponse({"message" : "NOT_EXISTS_MID"}, status=400)
        if View.objects.filter(mid = request.POST["mid"]).exists():
            return JsonResponse({"message" : "ALREADY_ADD_MID"}, status=400)
        upk = User.objects.get(pk=user_pk)
        # mpk = Movie.objects.get(pk=movie_pk)
        View.objects.create(
            uid = upk,
            mid = movie_pk,
            point = request.POST["point"],
            review = request.POST["review"]
        ).save()

        return JsonResponse({"message" : "VIEW_ADD_SUCCESS"},status=200)
    except KeyError:
        return JsonResponse({"message" : "JOIN_FAILED"},status=400)

#사용자 장르 선호도 분석
@api_view(['POST']) 
def my_preferGenre_list(request):
    dic = { '모험': 0, 
            '판타지': 0, 
            '애니메이션': 0,
            '드라마':0,
            '공포':0,
            '액션':0,
            '코미디':0,
            '역사':0,
            '서부':0,
            '스릴러':0,
            '범죄':0,
            '다큐멘터리':0,
            'SF':0,
            '미스터리':0,
            '음악':0,
            '로맨스':0,
            '가족':0,
            '전쟁':0,
            'TV 영화':0,
        }

    uid = request.data.get('uid')
    view = View.objects.filter(uid=uid).values()
    for n in view:
        mid = n['mid']
        #mid_list = Movie_genre_list.objects.filter(movie_id=mid).values()
        mid_list=extract_genre(mid)
        for k in range(len(mid_list)):
            # gid=k['genre_id_id']
            # gid_list = Genre.objects.filter(id=gid).values()
            gname=mid_list[k]['keyword']
            #dic['모험'] +=1
            dic[gname] +=1  
            

    res =sorted(dic.items(), key=(lambda x:x[1]),reverse=True)
    #print(type(res))
    # result_set = []
    # for i in range(len(res)):
    #     result_set.append(res[i]) 
    #pp = res[0]
    ##first() : queryset 결과의 내용 중 가장 첫번째 row만 반환
    result = dict(res)
    #print(pp)
    return JsonResponse({"message" : result},status=200)    

#사용자 선호 장르에 따른 영화 추천 + 평점 내림차순 정렬
@api_view(['POST'])
def genre_recommend(request):
    #장르 > 장르id > 영화 id
    resultsort = [] 
    genre_name = request.data.get('genre_name')
    genre = Genre.objects.filter(name=genre_name).values()
    genre_id = genre[0]['id']
    # bb = Movie.objects.select_related('id').all()
    query_set = Movie_genre_list.objects.filter(genre_id_id=genre_id).values()
    for row in query_set :
        mid = row['movie_id_id']
        mid_filter_list = Movie.objects.filter(id = mid).values('id').distinct() ##쿼리셋 리스트
        for kk in mid_filter_list.values_list():
            # print(mid_filter_list)
            # mid_filter_list = list(mid_filter_list)
            # resultsort.append(mid_filter_list)
            
            add_set = {
                    "title" : kk[1],
                    "original_title" : kk[2],
                    "poster_path" : kk[3],
                    "popularity" : kk[4],
                    "release_date" : kk[5],
                    "runtime" : kk[6],
                    "vote_average" : kk[7],
                    "overview" : kk[8]
                }
            # print(add_set)
            resultsort.append(add_set)
    resultsort = sorted(resultsort, key=lambda result_set: (result_set["vote_average"],result_set['release_date']), reverse=True  )      
    result_set =[]
    if(len(resultsort)>=20):    
        for i in range(20):
            result_set.append(resultsort[i])
    return JsonResponse({"message" : result_set},status=200)   

#영화 장르 추출
def extract_genre(movieid):
    tmdb_api = TMDB_API('d9560dbd976c10837a85763f71ab79b1')
    url=tmdb_api.get_url(movieid)
    movies_dict = requests.get(url)
    movie = movies_dict.json()
    set = []
    for i in range(len(movie['genres'])) :
            add_set = {
                "keyword" : movie['genres'][i]['name']
            }
            set.append(add_set)
    return set

# 영화(movie id) 존재확인
def movie_exist_check(movieid):
    tmdb_api = TMDB_API('d9560dbd976c10837a85763f71ab79b1')
    url=tmdb_api.get_url(movieid)
    movies_dict = requests.get(url)
    if(movies_dict.status_code == 401 or movies_dict.status_code == 404):
        return False
    else:
        return True

# TMDB 영화정보요청 API
class TMDB_API():
    url = 'https://api.themoviedb.org/3/movie/'
    key = 'd9560dbd976c10837a85763f71ab79b1'

    def __init__(self,key):
        self.key = key

    def get_url(self,num):
        return f'{self.url}{num}?api_key={self.key}&language=ko-KR'
        #https://api.themoviedb.org/3/movie/3?api_key=d9560dbd976c10837a85763f71ab79b1&language=ko-KR


###DB DATA IMPORT / NOW-47PAGE / POPULAR -50PAGE / UPCOMING -18PAGE
class URLMaker():
    url = 'https://api.themoviedb.org/3/movie/upcoming'
    key = 'd9560dbd976c10837a85763f71ab79b1'

    def __init__(self,key):
        self.key = key

    def get_url(self,num):
        return f'{self.url}?api_key={self.key}'

def movieInfo():
    url_maker = URLMaker('d9560dbd976c10837a85763f71ab79b1')
    page = 1
    while page < 19 : 
        url = url_maker.get_url(page)
        url_1 = f'{url}&language=ko-kr&page={page}'
        print(url_1)
        movies_dict = requests.get(url_1)
        movie = movies_dict.json()
        print()
        try:
            for i in range(len(movie['results'])):
                m_rst = movie['results'][i]
                if m_rst['overview'] and m_rst['adult'] == False:
                    new_movie = Movie()
                    if(Movie.objects.filter(id=m_rst['id']).exists() == True):
                        #print('********중복영화id'+str(m_rst[id]))
                        continue
                    new_movie.id = m_rst['id']
                    new_movie.title = m_rst['title']
                    new_movie.original_title = m_rst['original_title']
                    poster_path = m_rst['poster_path']
                    new_movie.poster_path= f'https://image.tmdb.org/t/p/w500/{poster_path}'
                    new_movie.release_date = m_rst['release_date']
                    new_movie.runtime = 0   
                    new_movie.popularity = m_rst['popularity']
                    new_movie.vote_average = m_rst['vote_average']
                    new_movie.overview = m_rst['overview']

                    new_movie.save()

                    for k in range(len(m_rst['genre_ids'])):
                        if(Movie_genre_list.objects.filter(movie_id_id=m_rst['id']).exists() == True):
                            print('********중복장르id'+str(m_rst[id]))
                            continue
                        Movie_genre_list.objects.create(movie_id_id=m_rst['id'], genre_id_id=m_rst['genre_ids'][k])
                        k += 1

                    
                    print(str(m_rst['title'])+'처리')
        except:
            pass
        page += 1