from django.db import models
from movie.models import Movie

class Slider(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="sliders")
    poster_slider = models.ImageField(upload_to='poster_slider/')
    show = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.name_en} - {self.order}'