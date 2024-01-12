from django.conf import settings
import pint

from django.db import models
from django.urls import reverse

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

    # def save(self, *args, **kwargs):
    #     qty = self.quantity
    #     qty_as_float , qty_as_float_success = number_to_str_to_float(qty)
    #     if qty_as_float_success:
    #         self.quantity = qty_as_float
    #     else:
    #     #super().save(*args, **kwargs)
    #     super.save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id":self.id})
    
    




    def convert_to_system(self, system="mks"):
        if self.quantity_as_float() is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float() * ureg(self.unit)
        print(measurement)
        return measurement
    

    def as_mks(self):
        # meter kilogram second
        measurement = self.convert_to_system(system="mks")
        return measurement.to_base_units()
    
    
    def as_imperial(self):
        # miles pounds seconds
        measurement = self.convert_to_system(system="imperial")
        return measurement.to_base_units()


