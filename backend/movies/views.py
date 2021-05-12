from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MovieListSerializer,MovieDetailSerializer,UserSerializer,GetUserSerializer
from .models import Movie,User

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

@api_view(['POST'])
def userid_check(request):
    email = request.data.get('email')
    # print(email)
    
    if email == None or User.objects.filter(email=email).exists():
        return Response({'fail'})
    
    return Response({'success'})

@api_view(['POST'])
def get_user(request):
    user = get_object_or_404(User, email=request.data.get('email'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def get_user_id(request):
    user = get_object_or_404(get_user_model(), id=request.data.get('id'))
    serializer = GetUserSerializer(user)
    return Response(serializer.data)    
