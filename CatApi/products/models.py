from django.db import models
from django.contrib.postgres.fields import ArrayField


class Categories(models.Model):
    name = models.CharField(
        max_length=150
    )
    visible = models.BooleanField()
    preview = models.ImageField(
        upload_to='images',
        null=True, blank=True
    )

    def __str__(self):
        return str(self.name)


class Products(models.Model):
    name = models.CharField(
        max_length=150
    )
    visible = models.BooleanField()
    description = models.CharField(
        max_length=400
    )
    price = models.IntegerField()
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return str(self.name)


class Params(models.Model):
    name = models.CharField(
        max_length=150
    )
    options = ArrayField(
        models.CharField(max_length=150)
    )
    product = models.OneToOneField(
        Products,
        on_delete=models.CASCADE,
        related_name='params'
    )

    def __str__(self):
        return str(self.name)


class ProductsImages(models.Model):
    image = models.ImageField(
        upload_to='images/products/', null=True, blank=True
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='images'
    )
