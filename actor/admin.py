from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fa')
    raw_id_fields = ('movie', 'created_by')
    search_fields = ('name_en', 'name_fa')
    readonly_fields = ('created',)
    ordering = ('name_en', 'name_fa')