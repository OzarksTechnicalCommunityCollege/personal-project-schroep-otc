from django.shortcuts import render
from .forms import FoodItemForm

# Create your views here.

# Render food entry form into a view
def enter_view(request):
    context = {}
    context['form'] = FoodItemForm
    return render(request, "home.html", context)

# Define "about" view
def about_view(request):
    return(render(request, 'about.html'))
