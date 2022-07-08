import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Shop(models.Model):

    name = models.CharField(max_length=40, unique=True)
    mcc = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=50, unique=True)
    shops = models.ManyToManyField(Shop, through='ShopProduct')

    def __str__(self):
        return self.name


class ShopProduct(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cash_back = models.FloatField(default=0, validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])


class Cheque(models.Model):

    @staticmethod
    def __pkgen():
        return random.randint(1, 1000)

    check_id = models.IntegerField(primary_key=True, default=__pkgen)
    user_id = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(ShopProduct, through='ChequeProduct')

    def __str__(self):
        return f'Чек №{self.pk}'


class ChequeProduct(models.Model):

    shop_product = models.ForeignKey(ShopProduct, on_delete=models.SET_NULL, null=True)
    cheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
    price = models.IntegerField()
