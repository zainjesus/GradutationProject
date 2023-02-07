from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = (
        ('Дом', 'Дом'),
        ('Квартира', 'Квартира'),
        ('Новостройка', 'Новостройка'),
    )
    title = models.CharField(default='Дом', choices=category, max_length=50)

    def __str__(self):
        return self.title


class House(models.Model):
    image = models.ImageField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    rooms_count = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rooms = models.CharField(default='3', choices=rooms_count, max_length=50)
    floor_count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )
    floor = models.CharField(default='3', choices=floor_count, max_length=50)

    def __str__(self):
        return f'{self.category}'


class Apartment(models.Model):
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    rooms_count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rooms = models.CharField(default='3', choices=rooms_count, max_length=50)

    def __str__(self):
        return f'{self.category}'
