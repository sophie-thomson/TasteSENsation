from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

COOKED_STATUS = ((0, "Not Cooked"), (1, "Cooked"))
SOURCE_SITES = [
    ("Accessible Chef", "Accessible Chef"),
    ("CookABILITY", "CookABILITY"),
]
COMMENT_CHOICES = [
    ("Love this recipe!", "Love this recipe!"),
    ("Delicious and easy to make.", "Delicious and easy to make."),
    ("OK, but probably won't make again.", "OK, but probably won't make again."),
    ("Too difficult for me, but might be OK for others", "Too difficult for me, but might be OK for others"),
]

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    source_site = models.CharField(choices=SOURCE_SITES)
    original_recipe = models.CharField()
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
    cooked_status = models.IntegerField(choices=COOKED_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def average_rating(self) -> float:
        return Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0
    
    def __str__(self):
        return f"{self.title}  |  {self.average_rating()}"


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    comment_selection = models.CharField(choices=COMMENT_CHOICES)
    own_comment = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.comment_selection}. {self.own_comment} by {self.author}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"