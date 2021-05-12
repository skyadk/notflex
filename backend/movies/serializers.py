from rest_framework import serializers
from .models import Movie,User

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #read_only_fields = ('article','like_users')
        exclude = ('id','overview')

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        #read_only_fields = ('article','like_users')
        #exclude = ('like_users','scrap_users')

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','nickname','preferGenre']