from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'source_site', 'cooked_status', 'created_on')
    search_fields = ['title', 'source_site']
    list_filter = ("cooked_status",)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions',)

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('recipe', 'comment_selection', 'own_comment', 'approved', 'author','created_on')
    # search_fields = ['title', 'source_site']
    list_filter = ("author",)
    # prepopulated_fields = {'recipe': ('title',), 'author': ('author',)}
    summernote_fields = ('own_comment', '',)


# Register your models here.
# admin.site.register(Recipe)--------------REMOVE
# admin.site.register(Comment)
