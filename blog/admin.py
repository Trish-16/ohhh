from django.contrib import admin
from .models import Category, Post #к файлам, которые в одном пакете модулей, обращаемся через '.'

admin.site.register(Category)
admin.site.register(Post)