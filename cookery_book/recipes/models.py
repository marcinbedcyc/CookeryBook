from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from PIL import Image


class Recipe(models.Model):
    SOUP = 'Soup'
    DESSERT = 'Dessert'
    SNACK = 'Snack'
    MAIN_COURSE = 'Main Course'
    APPETIZER = 'Appetizer'
    DRINK = 'Drink'
    BREAKFAST = 'Breakfast'
    PRESERVES = 'Preserves'
    SALADS = 'Salads'
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
    main_image = models.ImageField(
        upload_to='recipe_gallery', default='food.jpg')
    dish_kind = models.CharField(max_length=20, choices=KINDS, default=SNACK)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + str(self.pk)

    def save(self, *args, **kwargs):
        super().save()
        maxsize = (960, 640)
        img = Image.open(self.main_image.path)
        if img.height > 640 or img.width > 960:
            img.thumbnail(maxsize)
            img.save(self.main_image.path)


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
    PIECES = 'p'
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
        (PIECES, _('Pieces')),
    )
    MEASURES_DICT = {
        MILILITER: MILILITER,
        GRAM: GRAM,
        KILOGRAM: KILOGRAM,
        LITER: LITER,
        POUNDS: POUNDS,
        GLASS: _('Glass'),
        CUP: _('Cup'),
        PINCH: _('Pinch'),
        TEASPOON: _('Teaspoon'),
        SPOON: _('Spoon'),
        PIECES: _('Pieces'),
    }
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    measure = models.CharField(max_length=2, choices=MEASURES, default=GRAM)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return '%g' % (self.amount) + f" {self.MEASURES_DICT[self.measure] if self.MEASURES_DICT[self.measure] != 'Pieces' else '' } {self.name}"


class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    main_image = models.ImageField(
        upload_to='recipe_gallery', default='food.jpg')

    def __str__(self):
        return str(self.amout) + self.measure

    def save(self, *args, **kwargs):
        super().save()
        maxsize = (960, 640)
        img = Image.open(self.main_image.path)
        if img.height > 640 or img.width > 960:
            img.thumbnail(maxsize)
            img.save(self.main_image.path)
