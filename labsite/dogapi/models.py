from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Breed(models.Model):
    breed_sizes = {
        "T": "Tiny",
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }

    name = models.CharField(max_length=100,primary_key=True)
    size = models.CharField(max_length=1, choices=breed_sizes)
    friendliness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name