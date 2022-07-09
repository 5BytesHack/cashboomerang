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
    shop = serializers.StringRelatedField()

    class Meta:
        model = ShopProduct
        fields = ('shop', 'product', 'cashback')


class ChequeSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    products = ShopProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cheque
        fields = ('check_id', 'user_id', 'shop', 'products')


# class HistoryChequeSerializer(serializers.Serializer):
#
#     user_id = serializers.IntegerField()
#     cheque_id = serializers.IntegerField()
#     shop = serializers.CharField(max_length=100)
#
#     def validate(self, attrs):
#         user_id = attrs.get('user_id')
#         try:
#             cheques = Cheque.objects.get(user_id=user_id)
#         except Exception:
#             raise ValidationError


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
