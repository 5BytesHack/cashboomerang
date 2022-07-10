import os.path

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Shop, Product, ChequeProduct, Cheque, ShopProduct


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('name', 'mcc')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name',)


class ShopProductSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ShopProduct
        fields = ('product', 'cashback')


class ChequeSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    products = ShopProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cheque
        fields = ('check_id', 'user_id', 'shop', 'products')


class UploadFileSerializer(serializers.Serializer):

    file = serializers.FileField()

    def validate(self, attrs):
        file = attrs.get('file', None)
        filename, file_extension = os.path.splitext(file.name)

        if file and file_extension == '.csv':
            return file
