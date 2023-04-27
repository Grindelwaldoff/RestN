import random

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class SalesImage(models.Model):
    pic = models.ImageField(
        upload_to='images/sales',
    )


class Coord(models.Model):
    name = models.CharField(max_length=150)
    employee = models.CharField(max_length=250, null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    yacoord = ArrayField(models.CharField(max_length=150))

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs) -> None:
        try:
            int(self.tel)
            return super().save(*args, **kwargs)
        except Exception:
            raise ValidationError('Телефон должен содержать только цифры.')


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    id = models.CharField(
        max_length=150,
        primary_key=True,
        blank=True,
        editable=False
    )
    description = models.CharField(max_length=400)

    def save(self, *args, **kwargs) -> None:
        self.id = ''.join(random.choice(alphabet) for i in range(150))
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class PortfolioImage(models.Model):
    image = models.ImageField(
        upload_to='images/portfolio',
    )
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return str(self.portfolio)
