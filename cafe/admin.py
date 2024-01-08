from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Recipe, RecipeIngridents

User = get_user_model()

admin.site.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display =['id', 'name','user']
    readonly_fields = ['created', 'updated']
    raw_id_fields = ['user']

admin.site.register(RecipeIngridents)

