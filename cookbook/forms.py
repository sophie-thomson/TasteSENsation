from .models import Comment, Recipe
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    form_id = forms.CharField(widget=forms.HiddenInput(), initial='comment_form')
    
    class Meta:
        model = Comment
        fields = ('suggested_comment','own_comment',)
    
    
class RecipeForm(forms.ModelForm):

    featured_image = CloudinaryFileField()

    class Meta:
        model = Recipe
        

        fields = ('title', 'original_recipe', 'featured_image', 
            'ingredients', 'instructions', 'baking', 
            'mixing', 'frying', 'straining', 'microwaving', 
            'whisking', 'chopping', 'hob_use', )

        labels = {
            'title': 'Name of Dish',
            'original_recipe': 'Original Recipe Link',
            'featured_image': 'Recipe Photo',
            'baking': 'Recipe Involves Baking',
            'mixing': 'Recipe Involves Mixing',
            'frying': 'Recipe Involves Frying', 
            'straining': 'Recipe Involves Straining', 
            'microwaving': 'Recipe Involves Microwaving', 
            'whisking': 'Recipe Involves Whisking', 
            'chopping': 'Recipe Involves Chopping',
            'hob_use': 'Recipe Involves Using the Hob',
        }
        
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['original_recipe'].widget.attrs.update({ 'placeholder':
                "If your recipe is based on another recipe, add the link here" })
        # Sets inital content for ingredients field to be read by Summernote widget
        self.fields['ingredients'].initial = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"

        self.fields['instructions'].initial = "<p>1. Describe step 1</p><hr><p>2.  Describe step 2</p><hr><p>3.  Describe step 3</p><hr>"

        self.fields['featured_image'].widget.attrs.update({ 'placeholder':
                "{% if recipe.featured_image %}See current uploaded image below{% endif %}"})

        self.fields['featured_image'].options={ 
            'tags': "directly_uploaded",
            'format': "WEBP",
            'crop': 'fill', 'width': 600, 'height': 400,
            }