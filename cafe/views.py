from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_list_or_404 , get_object_or_404
from .models import Recipe, RecipeIngridents
from django import forms
from .forms import RecipeForm

# Create your views here.
#CURD -> Create, Update, Retrieve, Delete

@login_required
def recipe_create_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context={
        "object_list":qs
    }
    return render(request, "recipes/recipe_create.html", context)


@login_required
def recipe_detail_view(request):
    obj = get_list_or_404(Recipe, id = id, user=request.user)
    context={
        "object":obj
    }
    return render(request, "recipes/recipe_detail.html", context)

@login_required
def recipe_update_view(request):
    form = RecipeForm(request.POST or None)
    obj = get_object_or_404(Recipe, id = id, user=request.user)
    context={
        "form":form,
        "object":obj
    }
    if form.is_valid():
        form.save()
        context["message"] = "Recipe has been successfully updated!!!"

    return render(request, "recipes/recipe_update.html", context)

