from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe
from .models import RecipeIngridents
from django.contrib.auth.models import User


# Create your tests here.

def test_user_pw(self):
    checked= self.user_a.check_password('Django@123')
    self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setup(self):
        self.user_a = get_user_model().objects.create_user(username='Admin', password='Django@123')
        self.recipe_a = Recipe.objects.create(
            name='Pizza', 
            user=self.user_a,
 )
        self.recipe_b = Recipe.objects.create(
            name='Burger', 
            user=self.user_a,
        )
        self.recipe_ingredients_a = RecipeIngridents.objects.create(
            name='Chicken', 
            quantity = 1,
        )

    # def test_user_count(self):
    #     qs = User.objects.all()
    #     self.assertEqual(qs.count(), 2) 

    # def test_user_recipe_reverse_count(self):
    #     user = self.user_a
    #     qs = user.recipe_set.all()
    #     self.assertEqual(qs.count(), 2) 
    
    def test_recipe_ingrediants_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingridents_set.all()
        self.assertEqual(qs.count(), 1)


