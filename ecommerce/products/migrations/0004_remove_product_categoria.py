# Generated by Django 3.2.4 on 2021-06-08 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categoria',
        ),
    ]
