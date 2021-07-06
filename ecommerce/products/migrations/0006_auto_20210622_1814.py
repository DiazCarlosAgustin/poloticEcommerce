# Generated by Django 3.2.4 on 2021-06-22 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_remove_category_products'),
        ('products', '0005_product_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categoria',
        ),
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='categories.category'),
            preserve_default=False,
        ),
    ]
