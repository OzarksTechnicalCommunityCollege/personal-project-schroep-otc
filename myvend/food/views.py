from django.shortcuts import render
from .models import FoodItem

# Create your views here.

# Render food entry form into a view
def fooditem_list(request):
    items = (
        FoodItem.objects.select_related("food_type", "location")
        .all()
        .order_by("food_name")
    )
    return render(request, "food/home.html", {"items": items})

# Define "about" view
def about_view(request):
    return render(request, "about.html")

