# Generated by Django 4.1.4 on 2023-01-14 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0004_order_address_order_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-create_at', '-payment_status', '-payment_at'], 'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
    ]