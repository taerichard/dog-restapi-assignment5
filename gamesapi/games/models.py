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

