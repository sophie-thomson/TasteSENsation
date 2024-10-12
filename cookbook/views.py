from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Recipe, Rating, Comment
from .forms import CommentForm
from .forms import RecipeForm


def recipe_list(request):
    """
    Retrieves data from the recipe model to display a list of recipes which can
    be filtered by average_rating.

    The recipe.average_rating is retrived from the model to add a rating_filter
    value to each recipe and when requested by the user, creates a new
    filtered_recipes list to be passed back to the template.

    Django Paginator allows the list to be paginated and ensures rating_filter
    carries over multiple pages.
    """
    queryset = Recipe.objects.filter(recipe_approved=1).order_by("-created_on")

    rating_filter = request.GET.get("rating", None)

    if rating_filter is not None:
        try:
            rating_filter = int(rating_filter)

            filtered_recipes = []

            for recipe in queryset:
                average_rating, ratings_count = recipe.get_average_rating()
                recipe.average_rating = average_rating
                recipe.ratings_count = ratings_count

                if average_rating == rating_filter:
                    filtered_recipes.append(recipe)

            # Update queryset to be the filtered list
            queryset = filtered_recipes
        except ValueError:
            pass

    # Paginate the results
    for recipe in queryset:
        average_rating, ratings_count = recipe.get_average_rating()
        recipe.average_rating = average_rating
        recipe.ratings_count = ratings_count

    # Pagination
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get("page")
    recipes = paginator.get_page(page_number)

    return render(request, 'cookbook/index.html', {
        'recipes': recipes,
        'rating_filter': rating_filter,
        'is_paginated': recipes.has_other_pages(),
    })


def recipe_detail(request, slug):
    """
    Retrieves data from the recipe model to display additional details
    for a particular recipe.

    **Context**

    ``recipe``
        An instance of :model:`cookbook.Recipe`.
    ``user_rating``
        The unique combination of the current user and their rating_value
    ``average_rating``
        The aggregate average of all submitted ratings using django Avg
    ``ratings_count``
        The aggregate total of all ratings submitted using django Count
    ``comments``
        All instances of comments for that particular recipe
    ``comment_count``
        The aggregate total of all approved recipe.comments using django Count
    ``comment_form``
        Crispy form used to submit and edit a particular comment instance

    **Template:**

    :template:`cookbook/recipe_detail.html`
    """

    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)

    average_rating, ratings_count = recipe.get_average_rating()

    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe,
                                            user=request.user).first()
    else:
        user_rating = None  # No rating for anonymous users

    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    comment_form = CommentForm()

    # If the user submits a rating
    if request.method == "POST":
        form_id = request.POST.get("form_id")

        if form_id == "rating_form":
            rating_value = request.POST.get("rating")

            # Update or create the rating for this unique user and recipe
            Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={"rating": rating_value}
            )

            return redirect("recipe_detail", slug=slug)

        elif form_id == "comment_form":
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.recipe = recipe
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )

                # Redirect to the same page after rating
                return redirect("recipe_detail", slug=slug)

    return render(request, "cookbook/recipe_detail.html", {
        "recipe": recipe,
        "user_rating": user_rating,
        "average_rating": average_rating,
        "ratings_count": ratings_count,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return redirect("recipe_detail", slug=slug)


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return redirect("recipe_detail", slug=slug)


def suggest_recipe(request):
    """
    view to suggest a new recipe using RecipeForm

    Uses slugify to format title into slug

    request.FILES included to ensure image file is included when
    retrieving the recipe
    """

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():

            recipe = form.save(commit=False)
            if not recipe.slug:
                recipe.slug = slugify(recipe.title)
            recipe.owner = request.user
            recipe.save()

            messages.success(request,
                             'Recipe suggestion submitted successfully!')

            return redirect("home")
        else:
            # If the form is invalid, display an error message
            messages.error(request,
                           'Error submitting the form. \
                           Please correct the errors below.')
    else:

        form = RecipeForm()

    return render(
        request, 'cookbook/suggest_recipe.html', {'form': form})


def recipe_edit(request, slug):
    """
    view to edit recipe as the recipe owner
    """
    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid() and recipe.owner == request.user:
            form.save(commit=False)
            recipe.recipe_approved = 0
            form.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)

    return render(
        request, 'cookbook/recipe_edit.html', {
            'form': form,
            'recipe': recipe,
        }
    )


def recipe_delete(request, slug):
    """
    view to delete recipe
    """
    queryset = Recipe.objects
    recipe = get_object_or_404(queryset, slug=slug)

    if recipe.owner == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')

    return redirect("home")
