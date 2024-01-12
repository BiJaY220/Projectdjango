from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_list_or_404 , get_object_or_404
from .models import Recipe, RecipeIngridents
from django import forms
from .forms import RecipeForm, RecipeIngredientForm

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
    form_2 = RecipeIngredientForm(request.POST or None)
    obj = get_object_or_404(Recipe, id = id, user=request.user)
    ingridents_forms = []
    for ingridents_obj in obj.recipeingridents_set.all():
        ingridents_forms.append(RecipeIngredientForm(request.POST or None))

    context={
        "form":form,
        "form_2": form_2,
        "ingridents_forms": ingridents_forms,
        "object":obj
    }
    if all([form.is_valid(), form_2.is_valid()]):
        form.save(commit=False)
        form_2.save(commit = False)
        print =("form", form.cleaned_data)
        context["message"] = "Recipe has been successfully updated!!!"

    return render(request, "recipes/recipe_update.html", context)

