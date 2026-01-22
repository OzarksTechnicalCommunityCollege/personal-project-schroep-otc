from django.db import models
from django.utils import timezone

# Create Food model 
class Food(models.Model):
    name = models.CharField(max_length=50)
    calories = models.PositiveIntegerField() # using PositiveIntegerField since I want it to be 0 or positive
    fat = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fiber = models.PositiveIntegerField()
    purine = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    curr_date = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name