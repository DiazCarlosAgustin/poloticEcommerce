# Generated by Django 3.2.4 on 2021-06-08 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
    ]
