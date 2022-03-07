"""
Book: Building RESTful Python Web Services
"""
from django.db import models

class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large')
    )
    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True
    size = models.CharField(
        choices=SIZE_CHOICES,
        max_length=10
    )
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()

class Dog(models.Model):
    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed, 
        related_name='dogs', 
        on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200) 
    favoriteFood = models.CharField(max_length=200)
    favoriteToy = models.CharField(max_length=200) 


class GameCategory(models.Model):
    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True
    game_category = models.ForeignKey(
        GameCategory, 
        related_name='games', 
        on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='', unique=True) # Adding unique argument and set it to true
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player, 
        related_name='scores', 
        on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        # Order by score descending
        ordering = ('-score',)
