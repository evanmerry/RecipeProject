from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Recipe, Category, SkillLevel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'app/recipe_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['query'] = query
        if query:
            filtered_recipes = Recipe.objects.filter(title__icontains=query)
        else:
            filtered_recipes = Recipe.objects.all()
        context['recipes'] = filtered_recipes

        context['total_recipes'] = Recipe.objects.count()
        context['total_categories'] = Category.objects.count()
        context['total_skill_levels'] = SkillLevel.objects.count()
        context['total_authors'] = Author.objects.count()
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'app/recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'category', 'skill_level', 'ingredient', 'instruction', 'skill_level']
    template_name = 'app/recipe_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['skill_levels'] = SkillLevel.objects.all()
        return context
    def form_valid(self, form):
        user = self.request.user
        author = user.author
        form.instance.author = author
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'author', 'category', 'skill_level', 'ingredient', 'instruction', 'skill_level']
    template_name = 'app/recipe_update.html'

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app/recipe_delete.html'
    success_url = reverse_lazy('recipe')





