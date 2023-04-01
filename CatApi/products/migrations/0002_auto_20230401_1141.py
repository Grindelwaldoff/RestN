# Generated by Django 3.2.18 on 2023-04-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='param',
            name='product',
        ),
        migrations.AddField(
            model_name='param',
            name='product',
            field=models.ManyToManyField(related_name='params', to='products.Product'),
        ),
    ]
