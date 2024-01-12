from django.urls import path

from .views import recipe_create_view, recipe_detail_view, recipe_update_view


app_name = "recipe"
urlpatterns = [
    path("", recipe_detail_view, name="recipe-detail"),
    path("create/", recipe_create_view, name="recipe-create"),
    path("<int:id>/", recipe_detail_view, name="recipe-detail"),
    path("<int:id>/update/", recipe_update_view, name="recipe-update"),



]