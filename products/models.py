from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    video = models.CharField(max_length=100, null=True)
    price = models.PositiveBigIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField()
    square = models.CharField(max_length=30)
    living_space = models.FloatField(null=True)
    ceiling_height = models.FloatField()
    floor = models.IntegerField()
    repair = models.CharField(max_length=100)
    furniture = models.CharField(max_length=100)
    bathroom = models.CharField(max_length=100)
    window = models.CharField(max_length=100)
    warm_floor = models.CharField(choices=(
        ('Да', 'Да'),
        ('Нет', 'Нет')
    ), max_length=50)
    balcony = models.CharField(choices=(
        ('Балкон', 'Балкон'),
        ('Лоджия', 'Лоджия')
    ),max_length=50)
    description = models.CharField(max_length=255)