# Generated by Django 4.1.4 on 2023-03-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_rooms_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]