from django.shortcuts import get_object_or_404, render
from .models import Food
from django.http import Http404

# Create your views here.

# Generic view
def food_list(request):
    foods = Food.all()
    return render(
        request,
        'myvend/food/list.html',
        {'foods': foods}
    )

# Display a single food
def food_detail(request, id):
    food = get_object_or_404(
        Food,
        id=id
    )
    return render(
        request,
        'myvend/food/detail.html',
        {'food': food}
    )