from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace= 'home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('movie/', include('movie.urls', namespace='movie')),
    path('actor/', include('actor.urls', namespace='actor')),
    path('comment/', include('comment.urls', namespace='comment'))
]
