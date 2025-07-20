from django.db import models
from accounts.models import User
from movie.models import Movie
from django.urls import reverse

class Actor(models.Model):
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo_actor/')
    wikipedia_url = models.URLField()
    movie = models.ManyToManyField(to=Movie,related_name='actors')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='actors')
    
    def get_absolute_url(self):
        return reverse('actor:show_all_actor_role_played', args=[self.id])
    
    def get_photo_url(self):
        return self.photo.url

    def __str__(self):
        return f'{self.name_fa}'