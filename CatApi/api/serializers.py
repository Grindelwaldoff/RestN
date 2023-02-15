from rest_framework import serializers

from products.models import Categories, Products, Params


class ParamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Params
        fields = ('name', 'options')


class ProductsSerializer(serializers.ModelSerializer):
    params = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = (
            'name', 'visible', 'description',
            'images', 'price', 'params'
        )

    def get_params(self, obj):
        return ParamsSerializer(obj.params).data

    def get_images(self, obj):
        return obj.images.all().values_list("image", flat=True)


class CategoriesSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Categories
        fields = ('name', 'visible', 'preview', 'items')

    def get_items(self, obj):
        return ProductsSerializer(
            obj.products, many=True, context=self.context
        ).data
