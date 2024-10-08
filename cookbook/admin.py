from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'owner', 'created_on', 'recipe_approved')
    search_fields = ['title', 'owner', 'recipe_approved']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('recipe', 'suggested_comment','own_comment', 'approved', 'author','created_on')
    # search_fields = ['title', 'source_site']
    list_filter = ("author",)
    # prepopulated_fields = {'recipe': ('title',), 'author': ('author',)}
    summernote_fields = ('own_comment',)


# Register your models here.

