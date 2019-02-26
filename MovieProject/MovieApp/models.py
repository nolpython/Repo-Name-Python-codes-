from django.db import models

class MyMovieModel(models.Model):
    rdate = models.DateField()
    movieName = models.CharField(max_length=50)
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    rating = models.IntegerField()
