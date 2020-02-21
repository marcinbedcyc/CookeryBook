from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    ordering = ['-created_date']
    paginate_by = 3
