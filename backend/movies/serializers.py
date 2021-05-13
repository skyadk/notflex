from rest_framework import serializers
from .models import Movie,User, View,Genre,Movie_genre_list

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
    class Meta:
        model = User
        fields = '__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetViewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        #fields = '__all__'
        fields = ['id','uid_id','mid_id','point','review']