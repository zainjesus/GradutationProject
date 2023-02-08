# Generated by Django 4.1.5 on 2023-02-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_apartment_title_remove_house_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AlterField(
            model_name='house',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
