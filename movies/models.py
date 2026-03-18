from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default='')
    color_start = models.CharField(max_length=7, default='#6c757d')
    color_end = models.CharField(max_length=7, default='#495057')
    icon = models.CharField(max_length=10, default='🎬')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=500)
    duration = models.IntegerField(help_text="Duration in minutes")
    poster_color_start = models.CharField(max_length=7, default='#1a1a2e')
    poster_color_end = models.CharField(max_length=7, default='#16213e')

    def __str__(self):
        return f"{self.title} ({self.year})"

    @property
    def duration_formatted(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        return f"{minutes}m"

    class Meta:
        ordering = ['-rating', 'title']
