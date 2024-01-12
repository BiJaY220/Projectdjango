from django import forms
from .models import Recipe , RecipeIngridents

class RecipeForm(forms.ModelForm):
   class Meta:
      model = Recipe
      fields = [
         'name',
         'description',
         'directions',
      ]

class RecipeIngredientForm(forms.Form):
   model = RecipeIngridents
   fields = [
      'name',
      'quantity',
      'unit',
   ]


   # name = forms.CharField()
   # quantity = forms.IntegerField()
   # unit = forms.CharField()