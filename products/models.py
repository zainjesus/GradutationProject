from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = (
        ('Дом', 'Дом'),
        ('Квартира', 'Квартира'),
        ('Новостройка', 'Новостройка'),
    )

    title = models.CharField(default='Дом', choices=category)

    def __str__(self):
        return self.title


class House(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rooms = models.CharField(default='3', choices=category)
    floor_count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    floor = models.CharField(default='3', choices=floor_count)

    def __str__(self):
        return f'{self.title}'


class Apps(models.Model):
    title = models.CharField(max_length=55)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)

    count = (
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rooms = models.CharField(default='3', choices=category)

    def __str__(self):
        return f'{self.title}'
