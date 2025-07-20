from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.MovieShowAllView.as_view(), name='show_all_movie'),
    path('<int:id>/', views.MovieDetailView.as_view(), name='detail_movie')
]