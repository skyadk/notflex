from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.id

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
        return str(self.id)

class User(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    pw = models.CharField(max_length = 20)
    nickname = models.CharField(max_length = 20)
    preferGenre = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.id)

class Movie_genre_list(models.Model):
    movie_id = models.ForeignKey(Movie, related_name="movie1", on_delete=models.CASCADE, db_column="movie_id")
    genre_id = models.ForeignKey(Genre, related_name="genre", on_delete=models.CASCADE, db_column="genre_id")
    #post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")

    def __str__(self):
        return self.id

class View(models.Model):
    uid = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, db_column="uid")
    mid = models.IntegerField()
    point = models.IntegerField()
    review = models.TextField()
    
    def __str__(self):
        return self.id