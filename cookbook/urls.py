from . import views
from django.urls import path


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path('<slug:slug>/', views.recipe_detail, name="recipe_detail"),
    path('<slug:slug>/comment_edit/<int:comment_id>', 
        views.comment_edit, name="comment_edit"),
    path('<slug:slug>/comment_delete/<int:comment_id>',
        views.comment_delete, name="comment_delete"),
] 