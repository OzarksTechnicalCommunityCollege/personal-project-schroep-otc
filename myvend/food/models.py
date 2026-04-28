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

# Create FoodItem model
class FoodItem(models.Model):
    food_name = models.CharField(max_length=50)
    food_type = models.ForeignKey(FoodType, on_delete=models.PROTECT, related_name="items")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="items")
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)
    tags = models.ManyToManyField(Tag, through="FoodItemTag", related_name="food_items")
    is_expiring_soon = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.food_name} ({self.quantity})"
    
# Create FoodItemTag model
class FoodItemTag(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tagged_on = models.DateField(auto_now_add=True)
    tagged_by = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = ("food_item", "tag")

    def __str__(self):
        return f"{self.food_item} — {self.tag}"

# Create NutritionInfo model
class NutritionInfo(models.Model):
    food_item = models.OneToOneField(
        FoodItem,
        on_delete=models.CASCADE,
        related_name="nutrition"
    )

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