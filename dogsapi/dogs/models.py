from django.core.validators import MaxValueValidator, MinValueValidator
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
    
    friendliness = models.IntegerField(
        default = 1, validators= [MaxValueValidator(5), MinValueValidator(1)])

    trainability = models.IntegerField(
        default = 1, validators= [MaxValueValidator(5), MinValueValidator(1)])

    sheddingamount = models.IntegerField(
        default = 1, validators= [MaxValueValidator(5), MinValueValidator(1)])
        
    exerciseneeds = models.IntegerField(
        default = 1, validators= [MaxValueValidator(5), MinValueValidator(1)])

    class Meta: 
        ordering = ('name',)
    def __str__(self):
        return self.name



class Dog(models.Model):
    # create gender options 
    genderoptions = (
        ("M","MALE"),
        ("F", "FEMALE")
    )

    name = models.CharField(max_length=200, unique=True) # Adding unique argument and set it to True
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed, 
        on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200) 
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200) 

    class Meta: 
        ordering = ('name',)
    def __str__(self):
        return self.name


