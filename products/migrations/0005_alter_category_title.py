# Generated by Django 4.1.5 on 2023-02-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_apartment_category_alter_house_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Дом', 'Дом'), ('Квартира', 'Квартира')], default='Дом', max_length=50),
        ),
    ]