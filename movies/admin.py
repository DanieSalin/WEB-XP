from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre', 'duration')
    list_filter = ('genre',)
    search_fields = ('title', 'director', 'producer', 'genre')
