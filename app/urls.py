from django.urls import path
from .views import HomePageView, AboutPageView, RecipeListView, RecipeDetailView, RecipeCreateView, RecipeDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('recipe/', RecipeListView.as_view(), name='recipe'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe_delete'),

]