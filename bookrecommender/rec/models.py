from django.db import models

# Create your models here.
class CustomUser(models.model):
    username = models.CharField(max_length=32)
    email = models.EmailField()

class Book(models.model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    genre = models.CharField(max_length=32)

class UserBookRating(models.model):
    name = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()