from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.fooditem_list, name="home"),
    path("about/", views.about_view, name="about"),
    path("search/", views.food_search, name="food_search"),
    #path("login/", views.user_login, name="login"), #previous login path
    # login / logout urls
    # path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    # # change password urls
    # path(
    #     'password-change/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='registration/password_change_form.html',
    #     ),
    #     name='password_change'
    # ),
    # path (
    #     'password-change/done/',
    #     auth_views.PasswordChangeDoneView.as_view(
    #         template_name='registration/password_change_done.html',
    #         ),
    #     name='password_change_done'
    # ),

    # #reset password urls
    # path(
    #     'password-reset/',
    #     auth_views.PasswordResetView.as_view(
    #         template_name='registration/password_reset.html'
    #     ),
    #     name='password_reset'
    # ),
    # path(
    #     'password-reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(
    #         template_name='registration/password_reset_done.html'
    #     ),
    #     name='password_reset_done'
    # ),
    # path(
    #     'password-reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(
    #         template_name='registration/password_reset_config.html'
    #     ),
    #     name='password_reset_config'
    # ),
    # path(
    #     'password-reset/complete/',
    #     auth_views.PasswordResetCompleteView.as_view(
    #         template_name='registration/password_reset_complete.html'
    #     ),
    #     name='password_reset_complete'
    # ),

    
    path('', include('django.contrib.auth.urls')),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]