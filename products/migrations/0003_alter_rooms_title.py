# Generated by Django 4.1.4 on 2023-03-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='title',
            field=models.CharField(choices=[('Студия', 'Студия'), ('Однокомнатная', 'Однокомнатная'), ('Двухкомнатная', 'Двухкомнатная'), ('Трехкомнатная', 'Трехкомнатная'), ('Четырехкомнатная', 'Четырехкомнатная'), ('Пятикомнатная', 'Пятикомнатная'), ('Пять и больше', 'Пять и больше')], max_length=50),
        ),
    ]
