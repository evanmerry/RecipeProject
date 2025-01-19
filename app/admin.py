from django.contrib import admin
from .models import Author, Category, Recipe, Food, SkillLevel

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Food)
admin.site.register(SkillLevel)

