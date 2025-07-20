from django.db import models
from accounts.models import User
from movie.models import Movie

class Comment(models.Model):
    user = models.ForeignKey(to=User , on_delete= models.CASCADE, related_name= "user_comments" )
    movie = models.ForeignKey(to=Movie , on_delete= models.CASCADE, related_name= "movie_comments" )
    reply = models.ForeignKey(to='self', on_delete= models.CASCADE, related_name= "reply_comments", blank= True, null= True)
    is_reply = models.BooleanField(default= False)
    content = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add= True)

    def get_username(self):
        if self.user.username:
            return self.user.username
        return 'کاربر سایت'

    def __str__(self):
        return f"{self.user} say on {self.movie} - {self.content[:30]}"