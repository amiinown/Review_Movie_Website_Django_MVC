from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('movie', 'order', 'show', 'created')
    raw_id_fields = ('movie',)
    readonly_fields = ('created',)
    ordering = ('order',)