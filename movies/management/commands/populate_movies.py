from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from .data import action, comedy, drama, horror, scifi, romance, thriller, animation, documentary, fantasy

POSTER_COLORS = [
    ('#0f0c29', '#302b63'), ('#700000', '#ff4e00'), ('#000000', '#434343'),
    ('#003973', '#e5e5be'), ('#000428', '#004e92'), ('#1a0533', '#4a0080'),
    ('#141e30', '#243b55'), ('#200122', '#6f0000'), ('#0f3460', '#533483'),
    ('#56ab2f', '#a8e063'), ('#f7971e', '#ffd200'), ('#f953c6', '#b91d73'),
    ('#4776e6', '#8e54e9'), ('#11998e', '#38ef7d'), ('#8e5a00', '#c8860a'),
    ('#41295a', '#2f0743'), ('#403b4a', '#e7e9bb'), ('#833ab4', '#fd1d1d'),
    ('#3a1c71', '#d76d77'), ('#232526', '#414345'),
]

GENRES_DATA = [
    {'name': 'Action', 'slug': 'action', 'description': 'Heart-pounding adventures filled with adrenaline, stunts, and epic battles.', 'color_start': '#ff416c', 'color_end': '#ff4b2b', 'icon': '🔥', 'data': action},
    {'name': 'Comedy', 'slug': 'comedy', 'description': 'Lighthearted, funny films guaranteed to make you laugh out loud.', 'color_start': '#f7971e', 'color_end': '#ffd200', 'icon': '😂', 'data': comedy},
    {'name': 'Drama', 'slug': 'drama', 'description': 'Emotionally rich stories exploring the full depth of the human experience.', 'color_start': '#7f00ff', 'color_end': '#e100ff', 'icon': '🎭', 'data': drama},
    {'name': 'Horror', 'slug': 'horror', 'description': 'Spine-chilling tales designed to terrify and thrill you.', 'color_start': '#1a1a2e', 'color_end': '#6f0000', 'icon': '👻', 'data': horror},
    {'name': 'Sci-Fi', 'slug': 'sci-fi', 'description': 'Mind-bending journeys through space, time, and future technology.', 'color_start': '#0f3460', 'color_end': '#533483', 'icon': '🚀', 'data': scifi},
    {'name': 'Romance', 'slug': 'romance', 'description': 'Heartwarming love stories that make you believe in magic.', 'color_start': '#f953c6', 'color_end': '#b91d73', 'icon': '❤️', 'data': romance},
    {'name': 'Thriller', 'slug': 'thriller', 'description': 'Edge-of-your-seat suspense packed with twists and shocking revelations.', 'color_start': '#232526', 'color_end': '#414345', 'icon': '🔪', 'data': thriller},
    {'name': 'Animation', 'slug': 'animation', 'description': 'Magical animated worlds for all ages, from heartwarming to epic.', 'color_start': '#11998e', 'color_end': '#38ef7d', 'icon': '🎨', 'data': animation},
    {'name': 'Documentary', 'slug': 'documentary', 'description': 'Fascinating real-world stories that educate, inspire, and challenge you.', 'color_start': '#8e5a00', 'color_end': '#c8860a', 'icon': '📽️', 'data': documentary},
    {'name': 'Fantasy', 'slug': 'fantasy', 'description': 'Enchanting worlds of magic, myth, and wonder beyond imagination.', 'color_start': '#4776e6', 'color_end': '#8e54e9', 'icon': '✨', 'data': fantasy},
]


class Command(BaseCommand):
    help = 'Populate the database with movie data (50+ per genre, sorted by IMDb rating).'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing old data...')
        Movie.objects.all().delete()
        Genre.objects.all().delete()

        total = 0
        for g in GENRES_DATA:
            genre = Genre.objects.create(
                name=g['name'], slug=g['slug'], description=g['description'],
                color_start=g['color_start'], color_end=g['color_end'], icon=g['icon'],
            )
            # Sort movies by IMDb rating descending before inserting
            movies = sorted(g['data'].MOVIES, key=lambda m: m[2], reverse=True)
            for i, m in enumerate(movies):
                c = POSTER_COLORS[i % len(POSTER_COLORS)]
                Movie.objects.create(
                    genre=genre,
                    title=m[0], year=m[1], rating=m[2], duration=m[3],
                    director=m[4], cast=m[5], description=m[6],
                    poster_color_start=c[0], poster_color_end=c[1],
                )
            total += len(movies)
            self.stdout.write(f'  OK {genre.name}: {len(movies)} movies')

        self.stdout.write(self.style.SUCCESS(f'\nDone! {total} movies across {len(GENRES_DATA)} genres.'))
