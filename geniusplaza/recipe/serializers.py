"""
Serializers for the app
"""

from rest_framework import serializers

from .models import Recipe, Ingredient, Step


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'text')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'step_text')


class RecipeSerializer(serializers.ModelSerializer):
    ingredient_recipe = IngredientSerializer(many=True)
    step_recipe = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'user', 'ingredient_recipe', 'step_recipe')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredient_recipe')
        steps_data = validated_data.pop('step_recipe')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        for step_data in steps_data:
            Step.objects.create(recipe=recipe, **step_data)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredient_recipe')
        ingredients = instance.ingredient_recipe.all()
        ingredients = list(ingredients)
        steps_data = validated_data.pop('step_recipe')
        steps = instance.step_recipe.all()
        steps = list(steps)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        for ingredient_data in ingredients_data:
            ingredient = ingredients.pop(0)
            ingredient.text = ingredient_data.get('text', ingredient.text)
            ingredient.save()
        for step_data in steps_data:
            step = steps.pop(0)
            step.step_text = step_data.get('step_text', step.step_text)
            step.save()
        return instance
