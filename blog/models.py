import json #импорты из пайтон

# импорты из джанго

# импорты из проекта

from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model): #модели категорий наследуются от models.model
    name = models.CharField(max_length=50, unique=True) #чтобы указать varchar - CharField, обязательно добавить max_length
    slug = models.SlugField(max_length=50, primary_key=True) #принимает не все символы, slug для идентификации (когда указываем primary key, id не устанавливается по умолчанию)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts') #если поле связано с таблицой из бд
    text = models.TextField() #текстовое поле без ограничений
    creation_date = models.DateTimeField(auto_now_add=True) #auto_now_add срабатывает при создании
    update_at = models.DateTimeField(auto_now=True) #при любом обновлении
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts') #обратная связь - из табл user достать все записи с ним связанные
    # всегда передавать get_user_model() на месте User
    image = models.ImageField(null=True, blank=True, upload_to='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-details', kwargs={'pk': self.pk}) #args=[str(self.id)]
