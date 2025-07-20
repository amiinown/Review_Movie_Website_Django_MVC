from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import ReplyForm
from movie.models import Movie
from .models import Comment
from django.contrib import messages

class AddReplyView(View):
    form_class = ReplyForm

    def post(self, request, movie_id, comment_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.movie = movie
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'پاسخ شما ثبت شد.', 'success')
        return redirect('movie:detail_movie', movie.id)