from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'year', 'rating', 'duration']
    list_filter = ['genre', 'year']
    search_fields = ['title', 'director']
