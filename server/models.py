from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=97)


class Movie(models.Model):
    title = models.CharField(max_length=97)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name="directed_movies")
    actors = models.ManyToManyField(Person, through="Play")
    year = models.IntegerField()


class Play(models.Model):
    actor = models.ForeignKey(Person)
    film = models.ForeignKey(Movie)
    role = models.CharField(max_length=97)

