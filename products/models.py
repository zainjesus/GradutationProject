from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    title = models.CharField(choices=(
        ('Дом', 'Дом'),
        ('Квартира', 'Квартира'),
        ('Новостройка', 'Новостройка')
    ), max_length=50)

    def __str__(self):
        return self.title


class Area(models.Model):
    title = models.CharField(choices=(
        ('Первомайский', 'Первомайский'),
        ('Октябрьский', 'Октябрьский'),
        ('Свердловский', 'Свердловский'),
        ('Ленинский', 'Ленинский ')
    ), max_length=50)

    def __str__(self):
        return self.title


class Rooms(models.Model):
    title = models.CharField(choices=(
        ('Студия', 'Студия'),
        ('Однокомнатная', 'Однокомнатная'),
        ('Двухкомнатная', 'Двухкомнатная'),
        ('Трехкомнатная', 'Трехкомнатная'),
        ('Четырехкомнатная', 'Четырехкомнатная'),
        ('Пятикомнатная', 'Пятикомнатная'),
        ('Шестикомнатная', 'Шестикомнатная')
    ), max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField(null=True)
    square = models.FloatField()
    living_space = models.FloatField()
    ceiling_height = models.FloatField()
    floor = models.IntegerField()
    repair = models.CharField(max_length=100)
    furniture = models.CharField(max_length=100)
    bathroom = models.CharField(max_length=100)
    window = models.CharField(max_length=100)
    warm_floor = models.CharField(choices=(
        ('Да', 'Да'),
        ('Нет', 'Нет')
    ), max_length=10)
    balcony = models.CharField(choices=(
        ('Балкон', 'Балкон'),
        ('Лоджия', 'Лоджия')
    ), max_length=10)
    description = models.CharField(max_length=255)