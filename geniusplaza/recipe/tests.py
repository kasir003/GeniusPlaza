from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import RecipeListView, RecipeView
from .models import User


# Create your tests here.
class RecipeTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="vamsi")

    def test_post_new_recipe(self):
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
        factory = APIRequestFactory()
        view = RecipeListView.as_view()
        request = factory.get('/recipes/')
        response = view(request)


