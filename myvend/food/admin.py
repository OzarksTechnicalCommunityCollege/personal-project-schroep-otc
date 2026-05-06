from django.contrib import admin
from .models import FoodItem,FoodItemTag
from catalog.models import FoodType, Location, Tag
from nutrition.models import NutritionInfo
from import_export.admin import ExportMixin





# Register your models here.
@admin.register(FoodItem)
class FoodItemAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["food_name", "food_type", "location", "quantity", "expiry_date"]
    list_filter = ["food_type", "location"]
    search_fields = ["food_name"]
    ordering = ["food_name"]
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(FoodType)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(FoodItemTag)
admin.site.register(NutritionInfo)