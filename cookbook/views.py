from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Rating, Comment
from .forms import CommentForm
from .forms import RecipeForm


# Create your views here.

class RecipeList(generic.ListView):
    template_name = "cookbook/index.html"
    paginate_by = 3


    def get_queryset(self):
        queryset = Recipe.objects.all().order_by("-created_on")
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

    average_rating = recipe.get_average_rating()
    
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    else:
        user_rating = None  # No rating for anonymous users
    # user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
    
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
                messages.add_message(
                    request, messages.SUCCESS,
                    'Comment submitted and awaiting approval'
                )

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
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

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
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect("recipe_detail", slug=slug)


def suggest_recipe(request):
    """
    view to suggest a new recipe using RecipeForm

    Uses slugify to format title into slug

    request.FILES included to ensure image file is included when retrieving the recipe

    """

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            
            recipe = form.save(commit=False)
            if not recipe.slug:
                recipe.slug = slugify(recipe.title)
            recipe.owner = request.user
            recipe.save()
            
            messages.success(request, 'Recipe suggestion submitted successfully!')
            
            return redirect('suggest_recipe')
        else:
            # If the form is invalid, display an error message
            messages.error(request, 'Error submitting the form. Please correct the errors below.')
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

