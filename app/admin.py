from django.contrib import admin
from .models import Category, Blog, Service
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Category)
admin.site.register(Blog, MarkdownxModelAdmin)
admin.site.register(Service)