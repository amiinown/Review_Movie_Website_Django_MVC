from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Movie, Genre
from comment.forms import CommentForm, ReplyForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F


class MovieShowAllView(View):
    template_name = 'movie/show_all_movie.html'

    def get(self, request):
        sort_by = request.GET.get('sort', 'release_date')
        valid_sort_fields = ['release_date', '-release_date', 'count_of_view', '-count_of_view', 'imdb_score', '-imdb_score']

        if sort_by not in valid_sort_fields:
            sort_by = 'release_date'

        movies = Movie.objects.all().order_by(sort_by)

        return render(request, self.template_name, {'movies':movies,'sort_by':sort_by})
class MovieDetailView(View):
    template_name = 'movie/detail_movie.html'
    form_class = CommentForm
    form_class_reply = ReplyForm

    def setup(self, request, *args, **kwargs):
        self.movie_instance = get_object_or_404(Movie, pk=kwargs['id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        Movie.objects.filter(id=self.movie_instance.id).update(count_of_view=F('count_of_view') + 1)
        actors = self.movie_instance.actors.all()
        comments = self.movie_instance.movie_comments.filter(is_reply=False)

        return render(request, self.template_name, {'movie':self.movie_instance, 'actors':actors,
                                                    'comments':comments, 'form':self.form_class, 'form_reply':self.form_class_reply})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.movie = self.movie_instance
            new_comment.save()
            messages.success(request, 'نظر شما ثبت شد.', 'success')
            return redirect('movie:detail_movie', self.movie_instance.id)
        