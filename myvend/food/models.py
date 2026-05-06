from django.db import models


# Create FoodItem model
class FoodItem(models.Model):
    food_name = models.CharField(max_length=50)
    food_type = models.ForeignKey(FoodType, on_delete=models.PROTECT, related_name="items")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="items")
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)
    tags = models.ManyToManyField(Tag, through="FoodItemTag", related_name="food_items")
    is_expiring_soon = models.BooleanField(default=False)

    class Meta:
        ordering = ["food_name"]

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