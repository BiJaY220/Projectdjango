from django.conf import settings

from django.db import models

"""
global ingridents
    recipe 
    1. create model
    -> ingridents
    -> recipe based ingridents

"""
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class RecipeIngridents(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=120)# pound , kg, gram, spoon, cup
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(auto_now_add=False,auto_now =True,null=True,blank=True)



