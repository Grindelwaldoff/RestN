from django.db import models
from django.contrib.postgres.fields import ArrayField


class Categorie(models.Model):
    name = models.CharField(
        max_length=150
    )
    visible = models.BooleanField()
    preview = models.ImageField(
        upload_to='images/category',
        null=True, blank=True
    )
    detail = models.BooleanField()
    visible = models.BooleanField()

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(
        max_length=150
    )
    visible = models.BooleanField()
    description = models.CharField(
        max_length=400, null=True, blank=True
    )
    price = models.IntegerField()
    params_props = ArrayField(
        models.CharField(max_length=150),
        null=True, blank=True
    )
    category = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return str(self.name)


class Param(models.Model):
    name = models.CharField(
        max_length=150
    )
    options = ArrayField(
        models.CharField(max_length=150)
    )
    price = ArrayField(
        models.CharField(max_length=250),
        blank=True, null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='params',
        unique=False
    )

    def __str__(self):
        return str(self.name)


class ProductsImage(models.Model):
    image = models.ImageField(
        upload_to='images/products/', null=True, blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return str(self.product)
