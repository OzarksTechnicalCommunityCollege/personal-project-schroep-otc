from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .models import FoodItem
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm, LoginForm

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

# Define login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not NONE:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})