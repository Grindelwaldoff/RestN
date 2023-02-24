from rest_framework import serializers

from products.models import Categorie, Product, Param
from portfolio.models import Portfolio, Coord, SalesImage


class CoordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coord
        fields = ('name', 'yacoord',)


class SalesImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesImage
        fields = ('pic',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data['pic']


class PortfolioSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ('name', 'id', 'description', 'images')

    def get_images(self, obj):
        request = self.context.get('request')
        objects = obj.images.all().values_list('image', flat=True)
        data = []
        for i in objects:
            data.append(
                request.build_absolute_uri(i).replace('portfolios/', 'images/')
            )
        return data


class ParamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Param
        fields = ('name', 'options')


class ProductsSerializer(serializers.ModelSerializer):
    params = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'visible', 'description',
            'images', 'price', 'params'
        )

    def get_params(self, obj):
        try:
            return ParamsSerializer(
                obj.params,
                many=True,
                context=self.context
            ).data
        except Exception:
            return []

    def get_images(self, obj):
        request = self.context.get('request')
        objects = obj.images.all().values_list('image', flat=True)
        data = []
        for i in objects:
            data.append(
                request.build_absolute_uri(i).replace('category/', 'images/')
            )
        return data


class CategoriesSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Categorie
        fields = ('name', 'visible', 'detail', 'preview', 'items',)

    def get_items(self, obj):
        return ProductsSerializer(
            obj.products, many=True, context=self.context
        ).data
