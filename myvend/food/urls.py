from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.fooditem_list, name="home"),
    path("about/", views.about_view, name="about"),
    path("search/", views.food_search, name="food_search"),
    #path("login/", views.user_login, name="login"), #previous login path
    # login / logout urls
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    # change password urls
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    path (
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    path("dashboard/", views.dashboard, name="dashboard"),
]