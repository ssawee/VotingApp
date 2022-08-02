from django.db import models
from django.urls import reverse


def get_character_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


def get_voting_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Character(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя персонажа')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия персонажа')
    last_name = models.CharField(max_length=255, verbose_name='Отчество персонажа')
    slug = models.SlugField(unique=True)
    age = models.PositiveSmallIntegerField(default=1, verbose_name='Возраст')
    photo = models.ImageField(blank=True, verbose_name='Фотография')
    info = models.TextField(blank=True, verbose_name='Краткая биография')

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return get_character_url(self, 'character_info')


class Voting(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название голосования')
    slug = models.SlugField(unique=True)
    start_date = models.DateTimeField(verbose_name='Дата начала голосования')
    end_date = models.DateTimeField(verbose_name='Дата окончания голосования')
    max_votes = models.PositiveIntegerField(default=1, verbose_name='Максимальное количество голосов')
    characters = models.ManyToManyField(Character, verbose_name='Персонажи голосования') 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_voting_url(self, 'voting_info')
