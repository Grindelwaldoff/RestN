from django.contrib import admin

from .models import (
    Products, ProductsImages,
    Categories, Params
)


admin.site.register(Products)
admin.site.register(ProductsImages)
admin.site.register(Categories)
admin.site.register(Params)
