from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('add_reply/<int:movie_id>/<int:comment_id>/', views.AddReplyView.as_view(), name='add_reply')
]