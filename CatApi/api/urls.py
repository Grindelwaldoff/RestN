from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    CategoryViewSet, SaleViewSet,
    CoordsViewSet, PortfolioViewSet
)


router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('sales', SaleViewSet, basename='sales')
router.register('coords', CoordsViewSet)
router.register('portfolios', PortfolioViewSet)


urlpatterns = [
    path('', include(router.urls))
]
