# Generated by Django 4.1.5 on 2023-02-12 14:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Первомайский', 'Первомайский'), ('Октябрьский', 'Октябрьский'), ('Свердловский', 'Свердловский'), ('Ленинский', 'Ленинский ')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Студия', 'Студия'), ('Однокомнатная', 'Однокомнатная'), ('Двухкомнатная', 'Двухкомнатная'), ('Трехкомнатная', 'Трехкомнатная'), ('Четырехкомнатная', 'Четырехкомнатная'), ('Пятикомнатная', 'Пятикомнатная'), ('Шестикомнатная', 'Шестикомнатная')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Дом', 'Дом'), ('Квартира', 'Квартира'), ('Новостройка', 'Новостройка')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.CharField(max_length=100, null=True)),
                ('price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('square', models.CharField(max_length=30)),
                ('living_space', models.FloatField(null=True)),
                ('ceiling_height', models.FloatField()),
                ('floor', models.IntegerField()),
                ('repair', models.CharField(max_length=100)),
                ('furniture', models.CharField(max_length=100)),
                ('bathroom', models.CharField(max_length=100)),
                ('window', models.CharField(max_length=100)),
                ('warm_floor', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=50)),
                ('balcony', models.CharField(choices=[('Балкон', 'Балкон'), ('Лоджия', 'Лоджия')], max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.area')),
                ('rooms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.rooms')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.type')),
            ],
        ),
    ]
