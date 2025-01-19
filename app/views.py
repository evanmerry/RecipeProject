from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Author, Recipe, Category, SkillLevel
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'app/recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'app/recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'author', 'category', 'skill_level', 'ingredient', 'instruction']
    template_name = 'app/recipe_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['categories'] = Category.objects.all()
        context['skill_levels'] = SkillLevel.objects.all()
        return context

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'author', 'category', 'skill_level', 'ingredient', 'instruction']
    template_name = 'app/recipe_update.html'

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app/recipe_delete.html'
    success_url = reverse_lazy('recipe')





