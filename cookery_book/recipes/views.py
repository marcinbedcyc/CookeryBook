from django.shortcuts import render
from .models import Recipe, RecipeImage, Ingredient
from django.views.generic import ListView, DetailView


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    ordering = ['-created_date']
    paginate_by = 3


class RecipeDetailView(DetailView):
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'
    model = Recipe


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    images = RecipeImage.objects.filter(recipe=recipe)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    context = {
        'recipe': recipe,
        'images': images,
        'ingredients': ingredients
    }
    return render(request, template_name='recipes/recipe_detail.html', context=context)
