from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MovieListSerializer,MovieDetailSerializer,MovieSerializer,UserSerializer,GetUserSerializer,GetViewListSerializer,GetUidSerializer
from .models import Movie,User, View,Movie_genre_list,Genre

import json

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
        
        curr_max_num = User.objects.all().count() + 949437
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
    print(view)
    for n in view:
        mid = n['mid_id']
        mid_list = Movie_genre_list.objects.filter(movie_id=mid).values()
        for k in mid_list:
            gid=k['genre_id_id']
            gid_list = Genre.objects.filter(id=gid).values()
            gname=gid_list[0]['name']
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
    result_set = [] 
    genre_name = request.data.get('genre_name')
    genre = Genre.objects.filter(name=genre_name).values()
    genre_id = genre[0]['id']
    # bb = Movie.objects.select_related('id').all()
    query_set = Movie_genre_list.objects.filter(genre_id_id=genre_id).values()
    for row in query_set :
        mid = row['movie_id_id']
        mid_filter_list = Movie.objects.filter(id = mid).values() ##쿼리셋 리스트
        for kk in mid_filter_list.values_list():
            # print(mid_filter_list)
            # mid_filter_list = list(mid_filter_list)
            # result_set.append(mid_filter_list)
            
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
            result_set.append(add_set)
    result_set = sorted(result_set, key=lambda result_set: result_set["vote_average"], reverse= True)        
    return JsonResponse({"message" : result_set},status=200)    