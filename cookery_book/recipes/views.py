from django.shortcuts import render
from .models import Recipe, RecipeImage, Ingredient
from django.views.generic import ListView, DetailView


PAGINATE_BY = 3


class BaseRecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipes'
    paginate_by = PAGINATE_BY


class RecipesListView(BaseRecipeListView):
    ordering = ['-created_date']


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


class SnacksListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.SNACK).order_by('-created_date')


class SoupsListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.SOUP).order_by('-created_date')


class DessertsListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.DESSERT).order_by('-created_date')


class MainCoursesListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.MAIN_COURSE).order_by('-created_date')


class AppetizersListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.APPETIZER).order_by('-created_date')


class DrinksListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.DRINK).order_by('-created_date')


class BreakfastListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.BREAKFAST).order_by('-created_date')


class SaladsListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.SALADS).order_by('-created_date')


class PreservesListView(BaseRecipeListView):
    def get_queryset(self):
        return Recipe.objects.filter(dish_kind=Recipe.PRESERVES).order_by('-created_date')
