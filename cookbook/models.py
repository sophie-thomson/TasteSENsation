from django.db import models
from django.contrib.auth.models import User

TAG_COOKED = ((0, "Not Cooked"), (1, "Cooked"))
APPLIANCE_CHOICES = [
    ("BK", "Baking"),
    ("MX", "Mixing"),
    ("FY", "Frying"),
    ("ST", "Straining"),
    ("MA", "Mashing"),
    ("WH", "Whisking"),
    ("CH", "Chopping"),
    ("BL", "Blending"),
]

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    appliances = models.CharField(choices=APPLIANCE_CHOICES)
    method = models.TextField()
    tag_cooked = models.IntegerField(choices=TAG_COOKED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
