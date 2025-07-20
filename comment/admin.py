from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'is_reply', 'created')
    raw_id_fields = ('user', 'movie', 'reply')
    search_fields = ('user', 'movie')
    readonly_fields = ('created',)