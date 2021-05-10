from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.TextField()
    poster_path = models.ImageField(upload_to=None, max_length=100)
    popularity = models.TextField()
    release_date = models.TextField()
    runtime = models.IntegerField()
    vote_average = models.IntegerField()
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title