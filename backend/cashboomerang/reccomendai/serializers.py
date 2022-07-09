import os.path

from rest_framework import serializers
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

    class Meta:
        model = ShopProduct
        fields = ('shop', 'product', 'cashback')


class ChequeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cheque
        fields = ('cheque_id', 'user_id', 'shop', 'products')


class ChequeProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChequeProduct
        fields = ('shop_product', 'cheque', 'price')


class UploadFileSerializer(serializers.Serializer):

    file = serializers.FileField()

    def validate(self, attrs):
        file = attrs.get('file', None)
        filename, file_extension = os.path.splitext(file.temporary_file_path())

        if file and file_extension == '.csv':
            return file
