from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.SearchMovieActorView.as_view(), name='search_movie_actor')
]