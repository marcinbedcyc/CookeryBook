from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipesListView.as_view(), name="recipes-list"),
    path("recipes/", views.RecipesListView.as_view(), name="recipes-list"),
    path("soups/", views.SoupsListView.as_view(), name="soups-list"),
    path("desserts/", views.DessertsListView.as_view(), name="desserts-list"),
    path("snacks/", views.SnacksListView.as_view(), name="snacks-list"),
    path("main_courses/", views.MainCoursesListView.as_view(), name="main-courses-list"),
    path("drinks/", views.DrinksListView.as_view(), name="drinks-list"),
    path("breakfast/", views.BreakfastListView.as_view(), name="breakfast-list"),
    path("salads/", views.SaladsListView.as_view(), name="salads-list"),
    path("appetizers/", views.AppetizersListView.as_view(), name="appetizers-list"),
    path("preserves/", views.PreservesListView.as_view(), name="preserves-list"),
    path("recipes/<int:pk>", views.recipe_detail, name="recipe-detail"),
]
