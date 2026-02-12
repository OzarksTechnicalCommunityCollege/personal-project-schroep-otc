from django.contrib import admin
from.models import FoodItem, FoodType, Location





# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["food_name", "food_type", "location", "quantity", "expiry_date"]
    list_filter = ["food_type", "location"]
    search_fields = ["food_name"]
    ordering = ["food_name"]
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(FoodType)
admin.site.register(Location)