from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


class SkillLevel(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    ingredient = models.TextField()
    instruction = models.TextField()
    skill_level = models.ManyToManyField(SkillLevel, related_name="skill_level")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})

class Food(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.name
