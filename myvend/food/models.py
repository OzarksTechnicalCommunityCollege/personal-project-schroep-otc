from django.db import models
from datetime import datetime

# Create FoodItem model 
class FoodItem(models.Model):
    food_name = models.CharField(max_length=50)
    type_id = models.PositiveIntegerField() # using PositiveIntegerField since I want it to be 0 or positive
    location_id = models.PositiveIntegerField()
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()

# Create FoodType model
class FoodType(models.Model):
    food_type = models.CharField(max_length=50)

# Create Location model
class Location(models.Model):
    location = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name