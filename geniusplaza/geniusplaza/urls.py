"""
geniusplaza URL Configuration
"""
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('recipe.urls')),
]
