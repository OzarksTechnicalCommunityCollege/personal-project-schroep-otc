from django.db import models

# Create NutritionInfo model
class NutritionInfo(models.Model):
    food_item = models.OneToOneField('food.FoodItem', on_delete=models.CASCADE, related_name="nutrition")

    fdc_id = models.IntegerField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)
    protein_g = models.FloatField(blank=True, null=True)
    carbs_g = models.FloatField(blank=True, null=True)
    fat_g = models.FloatField(blank=True, null=True)
    fiber_g = models.FloatField(blank=True, null=True)
    sugar_g = models.FloatField(blank=True, null=True)
    sodium_mg = models.FloatField(blank=True, null=True)

    serving_size = models.FloatField(blank=True, null=True)
    serving_unit = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Nutrition for {self.food_item.food_name}"