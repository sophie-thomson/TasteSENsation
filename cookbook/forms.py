from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, HTML
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

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['original_recipe'].widget.attrs.update({ 'placeholder':
                "If your recipe is based on another recipe, add the link here" }),
        self.fields['ingredients'].widget.attrs.update({ 'placeholder': 
                "List all the ingredients, including any measurements"}),
        self.fields['instructions'].widget.attrs.update({ 'placeholder':
                "Provide simple step by step instructions"}),

        self.helper = FormHelper()
        self.helper.layout = Layout(
                    'baking', 
                    'mixing', 
                    'frying', 
                    'straining', 
                    'microwaving', 
                    'whisking', 
                    'chopping', 
                    'hob_use',
        )