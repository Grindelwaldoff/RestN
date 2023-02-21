import base64
import json
import io

from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response

from products.models import Categorie
from portfolio.models import Portfolio, SalesImage, Coord
from .serializers import CategoriesSerializer, PortfolioSerializer, CoordSerializer, SalesImageSerializer


class List(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorie.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = CategoriesSerializer(
            self.queryset, context={"request": self.request}, many=True
        )
        return serializer_class


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class CoordsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class SaleViewSet(List):
    queryset = SalesImage.objects.all()
    serializer_class = SalesImageSerializer
