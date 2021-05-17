from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.movie_list),
    path('movie_list/<int:movie_pk>/', views.moive_detail),
    path('userid_check/',views.userid_check),
    path('get_user/',views.get_user),
    path('get_user_id/',views.get_user_id),
    path('my_view_list/<int:uid>/',views.my_view_list),
    path('join_user/',views.join_user),
    path('my_preferGenre_list/',views.my_preferGenre_list),
    path('genre_recommend/',views.genre_recommend)
]