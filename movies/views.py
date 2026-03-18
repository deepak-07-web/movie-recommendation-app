from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie


def home(request):
    genres = Genre.objects.all()
    return render(request, 'movies/home.html', {'genres': genres})


def recommendations(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    movies = Movie.objects.filter(genre=genre).order_by('-rating')
    genres = Genre.objects.all()
    return render(request, 'movies/recommendations.html', {
        'genre': genre,
        'movies': movies,
        'genres': genres,
    })
