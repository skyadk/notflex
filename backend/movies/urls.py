from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.movie_list),
    path('movie_list/<int:movie_pk>/', views.moive_detail),
]