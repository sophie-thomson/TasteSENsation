from django.shortcuts import render
from django.views import generic
from .models import Recipe, Rating
from django.http import HttpResponse


# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "cookbook/index.html"
    paginate_by = 3

    # Function to check if user has made any rating for each recipe and if so, 
    # saves to the list to display
    def get_recipes(self):
        recipes = Recipe.objects.all()
        for recipe in recipes:
            rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
            recipe.user_rating = rating.rating if rating else 0
        return recipes

def rate(request, recipe_id: int, rating: int) -> HttpResponse:
    recipe = Recipe.objects.get(id=recipe_id)
    # Deletes the existing rating for this user and recipe
    Rating.objects.filter(recipe=recipe, user=request.user).delete()
    # Creates a new rating
    recipe.rating_set.create(user=request.user, rating=rating)
    return index(request)
