from . import views
from django.urls import path


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
] 

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)