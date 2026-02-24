from django.shortcuts import render
from .models import FoodItem
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

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

# Define search view
def food_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = (
                FoodItem.objects.annotate(
                    search=SearchVector("food_type", "location"),
                )
                .filter(search=query)
            )

    return render(
        request,
        "food/search.html",
        {
            'form': form,
            'query': query,
            'results': results
        }
    )