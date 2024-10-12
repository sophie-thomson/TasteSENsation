from .models import Comment, Recipe
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    CommentForm defines the form content to be displayed in the
    recipe_detail template.

    Form includes a hidden field to identify form_id in
    used in recipe_detail view.

    This differentiates between the comment_form and the rating_form
    to manage different POST functions in the view.
    """
    form_id = forms.CharField(
        widget=forms.HiddenInput(), initial='comment_form'
    )

    class Meta:
        model = Comment
        fields = ('own_comment',)

        labels = {'own_comment': 'Enter your comment:', }


class RecipeForm(forms.ModelForm):
    """
    RecipeForm defines the form fields and layout to be displayed in the
    suggest_recipe and edit_recipe templates.

    Ingredients and instructions fields use Summernote widget to enable initial
    content to include html formatting to match rendered layout and styling in
    recipe_detail template.

    **NB: Summernote widget raises multiple html validation errors which cannot
    be targeted and resolved using project css styling. This is highlighted as
    a bug issue #55 in the TasteSENsation Kanban Board and noted in the
    project README.**
    """

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

        self.fields['original_recipe'].widget.attrs.update
        ({'placeholder':
            "If your recipe is based on another recipe, add the link here"})

        self.fields[
            'ingredients'
        ].initial = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"

        self.fields[
            'instructions'
        ].initial = "<p>1. <input type=checkbox>&nbsp;&nbsp;Describe step 1\
        </p><hr>\
        <p>2.  <input type=checkbox>&nbsp;&nbsp;Describe step 2</p>\
        <hr>\
        <p>3.  <input type=checkbox>&nbsp;&nbsp;Describe step 3</p>\
        <hr>\
        <p>4.  <input type=checkbox>&nbsp;&nbsp;Describe step 4</p>\
        <hr>\
        <p>5.  <input type=checkbox>&nbsp;&nbsp;Describe step 5</p><hr>"

        self.fields['featured_image'].options = {
            'tags': "directly_uploaded",
            'format': "WEBP",
            'crop': 'fill', 'width': 600, 'height': 400,
            }
