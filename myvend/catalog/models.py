from django.db import models

# Create FoodType model
class FoodType(models.Model):
    food_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.food_type

# Create Location model
class Location(models.Model):
    location = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.location

# Create Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
