from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MovieListSerializer,MovieDetailSerializer
from .models import Movie

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