from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Rating
from django.http import HttpResponse


# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "cookbook/index.html"
    paginate_by = 3

    # Function to 
    def get_recipes(self):
        """
        Checks if user has made any rating for each recipe and if so, saves to the list to display
        """
        recipes = Recipe.objects.all()
        for recipe in recipes:
            rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
            recipe.user_rating = rating.rating if rating else 0
        return recipes


def rate(request, recipe_id: int, rating: int) -> HttpResponse:
    """
    Deletes any existing rating submiited by the user
    Creates a new rating with the latest selection
    """
    recipe = Recipe.objects.get(id=recipe_id)
    Rating.objects.filter(recipe=recipe, user=request.user).delete()
    recipe.rating_set.create(user=request.user, rating=rating)
    return index(request)


def recipe_detail(request, slug):
    """
    Displays an individual :model:`recipe.Post`.

    **Context**

    ``recipe``
        An instance of :model:`cookbook.Recipe`.

    **Template:**

    :template:`cookbook/recipe_detail.html`
    """

    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "cookbook/recipe_detail.html",
        {"recipe": recipe},
    )
