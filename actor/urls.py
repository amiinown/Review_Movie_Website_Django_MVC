from django.urls import path
from . import views

app_name = 'actor'
urlpatterns = [
    path('', views.ActorShowAllView.as_view(), name='show_all_actor'),
    path('Roles/<int:id>/', views.ActorRolePlayedView.as_view(), name='show_all_actor_role_played')
]