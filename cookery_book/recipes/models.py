from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Recipe(models.Model):
    SOUP = 1
    DESSERT = 2
    SNACK = 3
    MAIN_COURSE = 4
    APPETIZER = 5
    DRINK = 6
    BREAKFAST = 7
    PRESERVES = 8
    SALADS = 9
    KINDS = (
        (SOUP, _('Soup')),
        (DESSERT, _('Dessert')),
        (SNACK, _('Snack')),
        (MAIN_COURSE, _('Main Course')),
        (APPETIZER, _('Appetizer')),
        (DRINK, _('Drink')),
        (BREAKFAST, _('Breakfast')),
        (PRESERVES, _('Preserves')),
        (SALADS, _('Salads'))
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    instructions = models.TextField()
    main_image = models.ImageField(upload_to='recipe_gallery', default='food.jpg')
    dish_kind = models.PositiveSmallIntegerField(choices=KINDS, default=SNACK)
    created_date = models.DateTimeField(default=timezone.now)


class Ingredient(models.Model):
    MILILITER = 'ml'
    LITER = 'l'
    GRAM = 'g'
    KILOGRAM = 'kg'
    POUNDS = 'lb'
    GLASS = 'gl'
    CUP = 'cp'
    PINCH = 'pi'
    TEASPOON = 'ts'
    SPOON = 's'
    MEASURES = (
        (MILILITER, MILILITER),
        (GRAM, GRAM),
        (KILOGRAM, KILOGRAM),
        (LITER, LITER),
        (POUNDS, POUNDS),
        (GLASS, _('Glass')),
        (CUP, _('Cup')),
        (PINCH, _('Pinch')),
        (TEASPOON, _('Teaspoon')),
        (SPOON, _('Spoon')),
    )
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    measure = models.CharField(max_length=2, choices=MEASURES, default=GRAM)
