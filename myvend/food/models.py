from django.db import models

# Create FoodType model
class FoodType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create Location model
class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create FoodItem model
class FoodItem(models.Model):
    food_name = models.CharField(max_length=50)
    food_type = models.ForeignKey(FoodType, on_delete=models.PROTECT, related_name="items")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="items")
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.food_name} ({self.quantity})"