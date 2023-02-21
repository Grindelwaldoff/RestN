from django.contrib import admin

from .models import (
    Product, ProductsImage,
    Categorie, Param
)
from portfolio.models import Portfolio, SalesImage, Coord, PortfolioImage


admin.site.register(Product)
admin.site.register(ProductsImage)
admin.site.register(Categorie)
admin.site.register(Param)
admin.site.register(Portfolio)
admin.site.register(SalesImage)
admin.site.register(Coord)
admin.site.register(PortfolioImage)
