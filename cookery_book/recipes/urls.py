from django.urls import path
from .views import RecipesListView, recipe_detail


urlpatterns = [
    path("", RecipesListView.as_view(), name="recipes-list"),
    path("recipes/", RecipesListView.as_view(), name="recipes-list"),
    path("recipes/<int:pk>", recipe_detail, name="recipe-detail"),
]
