from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.fooditem_list, name="home"),
    path("about/", views.about_view, name="about"),
    path("search/", views.food_search, name="food_search"),
    path("login/", views.user_login, name="login"),
]