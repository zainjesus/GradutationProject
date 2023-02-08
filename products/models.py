from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = (
        ('Дом', 'Дом'),
        ('Квартира', 'Квартира')
    )
    title = models.CharField(default='Дом', choices=category, max_length=50)

    def __str__(self):
        return self.title


class House(models.Model):
    image = models.ImageField(null=True)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    rooms = models.CharField(default='3', choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ), max_length=50)
    floor = models.CharField(default='3', choices=(
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ), max_length=50)

    def __str__(self):
        return f'{self.category}'


class Apartment(models.Model):
    image = models.ImageField(null=True)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    rooms = models.CharField(default='3', choices=(
        ('1', '2'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ), max_length=50)

    def __str__(self):
        return f'{self.category}'
