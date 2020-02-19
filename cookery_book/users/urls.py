from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.test, name="users-test"),
    path("register/", views.register, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="users-logout"),
    path('activate/(<uidb64>/<token>', views.activate, name='activate'),
]
