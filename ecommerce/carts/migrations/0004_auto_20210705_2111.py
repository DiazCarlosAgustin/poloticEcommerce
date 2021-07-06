# Generated by Django 3.2.4 on 2021-07-06 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210622_1814'),
        ('carts', '0003_auto_20210705_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='productos',
        ),
        migrations.AddField(
            model_name='cart',
            name='productos',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]