from django.db import models
from django.urls import reverse
from django.conf import settings

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author")
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
    image = models.ImageField(upload_to='recipe_images', default='fallback.png', blank=True)
    ingredient = models.TextField()
    instruction = models.TextField()
    skill_level = models.ManyToManyField(SkillLevel)
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
