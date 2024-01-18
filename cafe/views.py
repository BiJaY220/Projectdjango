from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_list_or_404 , get_object_or_404, redirect
from .models import Recipe, RecipeIngridents
from django import forms
from .forms import RecipeForm, RecipeIngredientForm
from django.forms.models import modelformset_factory 

# Create your views here.
#CURD -> Create, Update, Retrieve, Delete



@login_required
def recipe_list_view(request):## create -> list
    qs = Recipe.objects.filter(user=request.user)
    context={
        "object_list":qs
    }
    return render(request, "cafe/list.html", context)


@login_required
def recipe_detail_view(request, id = None):
    obj = get_list_or_404(Recipe, id=id , user=request.user)
    context={
        "object":obj
    }
    return render(request, "cafe/detail.html", context)

@login_required
def recipe_create_view(request):## create -> list
    form = RecipeForm(request.POST or None)
    context ={
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit= False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "cafe/create-update.html", context)


@login_required
def recipe_update_view(request, id = None):
    obj = get_object_or_404(Recipe, id = id, user=request.user)
    form = RecipeForm(request.POST or None, instance = obj)
    #form_2 = RecipeIngredientForm(request.POST or None)
    RecipeIngredientFormSet = modelformset_factory(RecipeIngridents, form=RecipeIngredientForm, extra=0)
    #ingridents_forms = []
    qs = obj.recipeingridents_set.all()
    # for ingridents_obj in obj.recipeingridents_set.all():
    #     ingridents_forms.append(RecipeIngredientForm(request.POST or None))
    formset = RecipeIngredientFormSet(request.POST or None, queryset=qs)
    context={
        "form":form,
        "formset":formset,# formset = ingridents_forms
        "object":obj
    }
    if all([form.is_valid(), formset.is_valid()]):
        # form.save(commit=False)
        # form_2.save(commit = False)
        # print =("form", form.cleaned_data)
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if child.recipe is None:
                print("Added new")
                child.recipe = parent
            child.save()
               
            # child.recipe = parent
            # child.save()

    context["message"] = "Recipe has been successfully updated!!!"
    return render(request, "cafe/create-update.html", context)


