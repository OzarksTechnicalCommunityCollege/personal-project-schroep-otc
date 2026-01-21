from django.contrib import admin
from.models import Food





# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'calories','purine','protein', 'fat', 'fiber', 'quantity']
    list_filter = ['name', 'location']
    search_fields = ['name', 'location', 'calories','purine','protein', 'fat', 'fiber']
    show_facets = admin.ShowFacets.ALWAYS