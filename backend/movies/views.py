from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MovieListSerializer,MovieDetailSerializer,UserSerializer,GetUserSerializer,GetViewListSerializer
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
    serializer = MovieDetailSerializer(movie)

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

