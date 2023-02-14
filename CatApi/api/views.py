from rest_framework import mixins, viewsets

from products.models import Categories
from .serializers import CategoriesSerializer


class List(mixins.ListModelMixin, viewsets.GenericViewSet):
    pass


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = CategoriesSerializer(
            self.queryset, context={"request": self.request}, many=True
        )
        return serializer_class
