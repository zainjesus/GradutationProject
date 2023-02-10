from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = (
        ('Дом', 'Дом'),
        ('Квартира', 'Квартира'),
    )
    title = models.CharField(default='Дом', choices=category, max_length=50)

    def __str__(self):
        return self.title


class House(models.Model):
    price = models.IntegerField()
    description = models.TextField()
    street = models.CharField(max_length=20)
    category = models.ManyToManyField(Category, blank=True)
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
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    floor_count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )
    floor = models.CharField(default='3', choices=floor_count, max_length=50)
    street = models.CharField(max_length=20)
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
