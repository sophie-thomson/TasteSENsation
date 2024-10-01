from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    form_id = forms.CharField(widget=forms.HiddenInput(), initial='comment_form')
    
    class Meta:
        model = Comment
        fields = ('suggested_comment','own_comment',)
    
    
class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title','original_recipe', 'featured_image', 'baking', 
        'mixing', 'frying', 'straining', 'microwaving', 'whisking', 
        'chopping', 'hob_use', 'ingredients','instructions',)
        labels = {
            'title': 'Name of Dish',
            'original_recipe': 'Original Recipe Link',
            'featured_image': 'Recipe Photo',
            'baking': 'Recipe Involves Baking',
            'mixing': 'Recipe Involves Mixing',
            'frying': 'Recipe Involves Frying', 
            'straining': 'Recipe Involves Straining', 
            'microwaving':'Recipe Involves Microwaving', 
            'whisking':'Recipe Involves Whisking', 
            'chopping': 'Recipe Involves Chopping',
            'hob_use':'Recipe Involves Using the Hob',
        }       