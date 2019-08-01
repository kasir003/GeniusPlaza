"""
Genius Plaza project views
"""

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .serializers import *


class RecipeListView(generics.ListCreateAPIView):
    """
    View to create and list Recipes
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete recipe based on primary key
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


@csrf_exempt
def user_recipe_list(request, pk):
    """
    View to retrive recipes based on user id
    :param request: json request
    :param pk: user id
    :return: serialized recipe info with user details
    """
    if request.method == "GET":
        try:
            recipe = Recipe.objects.get(user=pk)
            serializer = RecipeSerializer(recipe)
            return JsonResponse(serializer.data, safe=False)
        except User.DoesNotExist:
            return HttpResponse(status=404)
