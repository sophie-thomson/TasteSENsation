from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from cloudinary.models import CloudinaryField

COOKED_STATUS = ((0, "Not Cooked"), (1, "Cooked"))
SOURCE_SITES = [
    ("Accessible Chef", "Accessible Chef"),
    ("CookABILITY", "CookABILITY"),
    ("Other", "Other"),
]
APPROVAL_STATUS = ((0, "Submitted"), (1, "Approved"))

# Suggested comment feature removed from the app as not good ux
COMMENT_CHOICES = [
    ("Love this recipe!", "Love this recipe!"),
    ("Delicious and easy to make.", "Delicious and easy to make."),
    ("OK, but won't make again.", "OK, but won't make again."),
    ("Too difficult.", "Too difficult."),
]


class Recipe(models.Model):
    """
    Recipe model defines all recipe data rendered in index, recipe_detail,
    and recipe_edit templates.

    RecipeForm used in suggest_recipe and recipe_edit templates displays
    selected fields from this model and uploads the field values to the
    recipe model.

    get_average_rating() uses django Avg and Count packages  to get all ratings
    for that particular recipe.slug and return an aggregate average_rating and
    a total ratings_count for the recipe.
    """
    owner = models.ForeignKey(
        User,
        related_name="creator",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    source_site = models.CharField(choices=SOURCE_SITES, blank=True)
    original_recipe = models.CharField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    baking = models.BooleanField(default=False)
    mixing = models.BooleanField(default=False)
    frying = models.BooleanField(default=False)
    straining = models.BooleanField(default=False)
    microwaving = models.BooleanField(default=False)
    whisking = models.BooleanField(default=False)
    chopping = models.BooleanField(default=False)
    hob_use = models.BooleanField(default=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooked_status = models.IntegerField(
        choices=COOKED_STATUS,
        default=0
    )
    created_on = models.DateField(auto_now_add=True)
    recipe_approved = models.IntegerField(
        choices=APPROVAL_STATUS,
        default=0
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_average_rating(self) -> tuple:
        average = self.ratings.aggregate(Avg("rating"))["rating__avg"]
        ratings_count = self.ratings.aggregate(
            Count("rating")
        )["rating__count"]
        return (round(average, 1) if average else 0, ratings_count)


class Rating(models.Model):
    """
    Rating model defines all rating data rendered in index and recipe_detail
    templates.

    unique_together creates a list of lists which must be unique when
    considered together. Each user is able to submit only one rating per
    recipe so unique_together overwrites any previous rating for that user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        related_name="ratings",
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)

    class Meta:
        unique_together = ("recipe", "user")

    def __str__(self):
        return f"{self.user.username} gave {self.recipe.title}, \
        {self.rating} stars"


class Comment(models.Model):
    """
    Comment model defines all comment data rendered in recipe_detail
    template.

    **NB: suggested_comment field not used in deployed project as did
    not add positive UX and over-complicated comment functionality.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    suggested_comment = models.CharField(choices=COMMENT_CHOICES, blank=True)
    own_comment = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.own_comment} by {self.author}"
