# Generated by Django 3.2.4 on 2021-06-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_remove_category_products'),
        ('products', '0004_remove_product_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]