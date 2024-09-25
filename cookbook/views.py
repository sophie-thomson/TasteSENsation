from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Rating
from django.http import JsonResponse


# Create your views here.

class RecipeList(generic.ListView):
    # queryset = Recipe.objects.all().order_by("-created_on")
    template_name = "cookbook/index.html"
    paginate_by = 3


    def get_queryset(self):
        queryset = Recipe.objects.all().order_by("-created_on")
        # recipes = Recipe.objects.all()
        for recipe in queryset:
            recipe.average_rating = recipe.get_average_rating()

        return queryset


# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     for recipe in recipes:
#         recipe.average_rating = recipe.get_average_rating()
#     return render(request, 'cookbook/index.html', {'recipes': recipes})


# def get_user_rating(request, ):
#     """
#     Checks if user has made any rating for each recipe and if so, saves to the list to display
#     """
#     recipes = Recipe.objects.all()
#     for recipe in recipes:
#         user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
#         recipe.user_rating = rating.rating if rating else 0
#     return user_rating


# def rate(request, recipe_id: int, rating: int):
#     """
#     Deletes any existing rating submitted by the user
#     Creates a new rating with the latest selection
#     """
#     recipe = Recipe.objects.get(id=recipe_id)
#     Rating.objects.filter(recipe=recipe, user=request.user).delete()
#     recipe.rating_set.create(user=request.user, rating=rating)
#     return index(request)


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
    user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    average_rating = recipe.get_average_rating()

    # If the user submits a rating
    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        # Update or create the rating for this user and recipe
        Rating.objects.update_or_create(
            recipe=recipe,
            user=request.user,
            defaults={'rating': rating_value}  # If a rating exists, it will be updated
        )

        # Redirect to the same page after rating
        return redirect('recipe_detail', slug=slug)

    return render(
        request,
        "cookbook/recipe_detail.html", {
        # user_rating and average_rating added to the 'context' 
        # dictionary for recipe detail page
        "recipe": recipe,
        "user_rating": user_rating,
        "average_rating": average_rating
        },
    )
