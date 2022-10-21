from django.db import models
from markdownx.models import MarkdownxField

class Category(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=100)
    url = models.URLField()
    img = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title