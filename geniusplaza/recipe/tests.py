from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import User


# Create your tests here.
class RecipeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="vamsi")

    def test_get_all_recipes(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_post_new_recipe(self):
        # Arrange
        request = {
            "name": "Pasta",
            "user": 1,
            "ingredient_recipe": [
                {
                    "text": "salt, sphagetti, pesto, cream"
                }
            ],
            "step_recipe": [
                {
                    "step_text": "Add all of the above"
                }
            ]
        }

        response = self.client.post('/recipes/', request, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
