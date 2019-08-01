"""
URLS pointing to various views
"""

from django.urls import path

from recipe import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view()),
    path('recipe/<int:pk>/', views.RecipeView.as_view()),
    path('user/<int:pk>/', views.user_recipe_list),
]
