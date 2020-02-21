from django.urls import path
from .views import recipe_list, RecipesListView


urlpatterns = [
    path("", RecipesListView.as_view(), name="recipes-list"),
]
