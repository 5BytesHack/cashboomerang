import csv

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView, Response

from .models import ChequeProduct, Cheque, Product, Shop, ShopProduct
from .serializers import UploadFileSerializer


# Create your views here.


# class AdminAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#
#         return Response()


class AddChequesCSVAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadFileSerializer

    def post(self, request):
        if request.user['is_staff']:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            with open(request.data['file']) as f:
                reader = csv.reader(f)
                for row in reader:
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
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)




