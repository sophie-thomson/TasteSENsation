from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'owner', 'created_on', 'recipe_approved')
    search_fields = ['title', 'owner', 'recipe_approved']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions',)
    ordering = ('recipe_approved',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = (
        'recipe',
        'own_comment',
        'approved',
        'author',
        'created_on'
    )
    list_filter = ("author",)
    ordering = ('-created_on', 'approved',)
