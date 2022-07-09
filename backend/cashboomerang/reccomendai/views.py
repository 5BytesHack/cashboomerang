import csv

from django.db.models import Count
from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

from .models import ChequeProduct, Cheque, Product, Shop, ShopProduct
from .serializers import UploadFileSerializer


# Create your views here.


# class UserPurchaseHistoryAPI(ListAPIView):
#     permission_classes = (AllowAny,)
#     pagination_class = PageNumberPagination
#
#     def post(self, request):




# class AdminAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#
#         return Response()


class GetStatAdminAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_staff:
            most_popular_products = ChequeProduct.objects.values('shop_product').annotate(n=Count('shop_product')).order_by('-n')[:5]
            most_popular_shops = Cheque.objects.values('shop').annotate(n=Count('shop')).order_by('-n')[:5]
            data = {
                'most_popular_products': [],
                'most_popular_shops': []
            }
            for prod in most_popular_products:
                product = ShopProduct.objects.get(pk=prod['shop_product'])
                data['most_popular_products'].append({
                    'name': product.product.name,
                    'shop': product.shop.name,
                    'count': prod['n']
                })
            for shop in most_popular_shops:
                shopdb = Shop.objects.get(pk=shop['shop'])
                data['most_popular_shops'].append({
                    'name': shopdb.name,
                    'count': shop['n']
                })
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AddChequesCSVAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadFileSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            # serializer.save()
            with open(request.data['file'].temporary_file_path(), encoding='UTF-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        shop, created = Shop.objects.get_or_create(
                            name=row[4],
                            mcc=row[5]
                        )
                        product, created = Product.objects.get_or_create(
                            name=row[2]
                        )
                        shop_product, created = ShopProduct.objects.get_or_create(
                            shop=shop,
                            product=product
                        )
                        cheque, created = Cheque.objects.get_or_create(
                            check_id=row[1],
                            user_id=row[0],
                            shop=shop
                        )
                        res, created = ChequeProduct.objects.get_or_create(
                            shop_product=shop_product,
                            cheque=cheque,
                            price=int(row[3])
                        )
                    except ValueError:
                        pass
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AddCashBacksAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadFileSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        if request.user.is_staff:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            with open(request.data['file'].temporary_file_path(), encoding='UTF-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    shop, created = Shop.objects.get_or_create(
                        name=row[1],
                        mcc=row[2]
                    )
                    product, created = Product.objects.get_or_create(
                        name=row[0]
                    )
                    try:
                        shop_product = ShopProduct.objects.get(shop=shop, product=product)
                        shop_product.cashback = int(row[3])
                        shop_product.save(update_fields=['cashback'])
                    except ShopProduct.DoesNotExists:
                        shop_product = ShopProduct(shop=shop, product=product, cashback=int(row[3]))
                        shop_product.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class GetCashBacksCSVAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = ShopProduct.objects.all()
        file_name = 'cashbacks'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(file_name)
        with open('cashbacks.csv', mode='w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\r")
            writer.writerow(['ProductName', 'MerchantName', 'MCC', 'CashBack'])
            for shop_product in queryset:
                shop = shop_product.shop
                product = shop_product.product
                writer.writerow([product.name, shop.name, shop.mcc, shop_product.cashback])
        return response



