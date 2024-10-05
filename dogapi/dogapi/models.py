from django.db import models
from django.contrib.auth.models import User

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Breed(models.Model):
    breed_sizes = {
        "T": "Tiny",
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=1, choices=breed_sizes)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    def __str__(self):
        return self.name