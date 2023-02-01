# Generated by Django 4.1.4 on 2023-01-08 07:13

import app_product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.FileField(blank=True, upload_to='images/category_icons', validators=[app_product.models.validate_svg], verbose_name='Иконка SVG'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/category_images/', verbose_name='Изображение'),
        ),
    ]