# Generated by Django 4.1.4 on 2023-01-08 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0007_remove_category_icon_link_remove_category_image_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyproduct',
            options={'verbose_name': 'история просмотра товаров', 'verbose_name_plural': 'истории просмотра товаров'},
        ),
        migrations.AlterModelTable(
            name='historyproduct',
            table='history_products',
        ),
    ]