from django.db import models
from django.contrib.auth.models import User

COOKED_STATUS = ((0, "Not Cooked"), (1, "Cooked"))
SOURCE_SITES = [
    ("AC", "Accessible Chef"),
    ("CA", "CookABILITY"),
    ("A2L", "Able2Learn"),
    ("AGU", "Autism Grown Up"),
]

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    source_site = models.CharField(choices=SOURCE_SITES)
    original_recipe = models.SlugField()
    baking = models.BooleanField(default=False)
    mixing = models.BooleanField(default=False)
    frying = models.BooleanField(default=False)
    straining = models.BooleanField(default=False)
    mashing = models.BooleanField(default=False)
    whisking = models.BooleanField(default=False)
    chopping = models.BooleanField(default=False)
    hob_use = models.BooleanField(default=False)
    average_rating = models.IntegerField(default=0)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooked_status = models.IntegerField(choices=COOKED_STATUS, default=0)
    want_to_try_tag = models.BooleanField(default=False)
    dislike_tag = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
