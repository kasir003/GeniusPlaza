"""
DB models for Genius Plaza Project
"""

from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    DB model for Recipes
    """
    name = models.TextField(help_text='Recipe name')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_recipe')


class Step(models.Model):
    """
    DB model for steps involved in a Recipe
    """
    step_text = models.TextField(help_text='String field to save the steps of recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, help_text='Receipe ID', related_name='step_recipe')

    def __str__(self):
        return '{}'.format(self.step_text)


class Ingredient(models.Model):
    """
    DB model for ingredients involved in a Recipe
    """
    text = models.TextField(help_text='Ingredients Text')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, help_text='Receipe ID', related_name='ingredient_recipe')

    def __str__(self):
        return '{}'.format(self.text)
