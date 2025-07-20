from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from omdbapi.movie_search import GetMovie
from datetime import datetime
from django.urls import reverse

class Movie(models.Model):
    MOVIE_TYPES = [
        ('movie', 'سینمایی'),
        ('series', 'سریال'),
    ]

    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    movie_type = models.CharField(max_length=6, choices=MOVIE_TYPES, default='movie')
    movie_genre = models.ManyToManyField(to='Genre', related_name='movies')
    poster = models.ImageField(upload_to='poster_movie/')
    background_poster = models.ImageField(upload_to='background_poster_movie/')
    trailer = models.FileField(upload_to='trailer_movie/')
    release_date = models.DateField(null=True, blank=True)
    imdb_score = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True, editable=True)
    count_of_view = models.PositiveIntegerField(null=True, blank=True, default=1)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='movies')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            if not self.imdb_score or not self.release_date:
                try:
                    movie = GetMovie('f1443bc6')
                    response = movie.get_movie(title=self.name_en)
                    
                    if 'imdbrating' in response and response['imdbrating'] != "N/A":
                        self.imdb_score = float(response['imdbrating'])
                    if 'released' in response and response['released'] not in ["N/A", None, ""]:
                        self.release_date = datetime.strptime(response['released'], '%d %b %Y').date()
                except Exception as e:
                    print(f"خطا در فراخوانی OMDB API: {e}")
        super().save(*args, **kwargs)

    def formatted_release_date(self):
        if self.release_date:
            return self.release_date.strftime('%Y/%m/%d')
        return "---"
    
    def get_absolute_url(self):
        return reverse('movie:detail_movie', args=[self.pk])
    
    def get_poster_url(self):
        return self.poster.url

    def __str__(self):
        return f'{self.name_en} - {self.release_date}'


class Review(models.Model):
    movie = models.OneToOneField(to=Movie, on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author.username}'
    
class Genre(models.Model):
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name_fa} - {self.name_en}'