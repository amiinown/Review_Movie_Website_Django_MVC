from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from actor.models import Actor
from movie.models import Movie
from django.conf import settings
from .models import Slider


class HomeView(View):
    def get(self, request):
        sliders = Slider.objects.filter(show=True).order_by('order')
        newest_movies = Movie.objects.order_by('-release_date')[:10]
        popular_movies = Movie.objects.order_by('-count_of_view')[:10]

        return render(request, 'home/index.html', {'sliders':sliders, 'newest_movies':newest_movies, 'popular_movies':popular_movies})

class SearchMovieActorView(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        results = {'movies': [], 'actors': []}

        if query:
            movies = Movie.objects.filter(Q(name_fa__icontains=query) | Q(name_en__icontains=query))[:10]

            actors = Actor.objects.filter(Q(name_fa__icontains=query) | Q(name_en__icontains=query))[:10]
    
            results['movies'] = [
                {
                    'id': movie.id,
                    'name_fa': movie.name_fa,
                    'name_en': movie.name_en,
                    'release_date': movie.release_date,
                    'poster_url': movie.get_poster_url(),
                } for movie in movies
            ]
    
            results['actors'] = [
                {
                    'id': actor.id,
                    'name_fa': actor.name_fa,
                    'name_en': actor.name_en,
                    'photo_url': actor.get_photo_url(),
                } for actor in actors
            ]

        return JsonResponse(results)