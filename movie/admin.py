from django.contrib import admin
from .models import Movie, Review, Genre
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'movie_type', 'release_date')
    raw_id_fields = ('created_by',)
    list_filter = ('movie_type', 'movie_genre')
    search_fields = ('name_en', 'name_fa')
    readonly_fields = ('created', 'modified')
    filter_horizontal = ('movie_genre',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'author', 'score')
    raw_id_fields = ('movie', 'author')
    search_fields = ('movie', )
    readonly_fields = ('created', 'modified')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name_fa', 'name_en', 'id')
    search_fields = ('name_fa', 'name_en')