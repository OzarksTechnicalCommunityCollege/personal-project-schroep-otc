from django.contrib import admin
from.models import FoodItem, FoodType, Location





# Register your models here.
admin.site.register(FoodItem)
admin.site.register(FoodType)
admin.site.register(Location)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'calories','purine','protein', 'fat', 'fiber', 'quantity']
    list_filter = ['name', 'location']
    search_fields = ['name', 'location', 'calories','purine','protein', 'fat', 'fiber']
    show_facets = admin.ShowFacets.ALWAYS