from django.db import models

# Create your models here.
class CustomUser(models.model):
    username = models.CharField(max_length=32)
    email = models.EmailField()

class Movie(models.model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.IntegerField()
    description = models.CharField(max_length=256)
    minutes = models.IntegerField()
    rating = models.FloatField()

class UserMovieRating(models.model):
    name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Genre(models.model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=32)

class Actor(models.model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.CharField(max_length=32)