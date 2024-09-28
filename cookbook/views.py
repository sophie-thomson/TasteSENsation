from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Recipe, Rating
from django.http import JsonResponse
from django import forms
from .forms import CommentForm


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


def recipe_detail(request, slug):
    """
    Displays an individual :model:`recipe.Post`.

    **Context**

    ``recipe``
        An instance of :model:`cookbook.Recipe`.
    ``user_rating``
        The unique combination of the current user and their rating_value 
    ``average_rating``
        The aggregate average of all submitted ratings using django Avg

    **Template:**

    :template:`cookbook/recipe_detail.html`
    """

    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)
    user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    average_rating = recipe.get_average_rating()
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    comment_form = CommentForm()

    # If the user submits a rating
    if request.method == "POST":
        form_id = request.POST.get("form_id")

        if form_id == "rating_form":
            rating_value = request.POST.get("rating")

            # Update or create the rating for this user and recipe
            Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={"rating": rating_value}  # If a rating exists, it will be updated
            )

            return redirect("recipe_detail", slug=slug)

        elif form_id == "comment_form":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.recipe = recipe
                comment.save()

                # Redirect to the same page after rating
                return redirect("recipe_detail", slug=slug)
    

    return render(
        request,
        "cookbook/recipe_detail.html", {
        # user_rating and average_rating added to the 'context' 
        # dictionary for recipe detail page
        "recipe": recipe,
        "user_rating": user_rating,
        "average_rating": average_rating,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )
