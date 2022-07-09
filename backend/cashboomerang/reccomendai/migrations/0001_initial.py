# Generated by Django 4.0.6 on 2022-07-08 21:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('mcc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cashback', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reccomendai.product')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reccomendai.shop')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(through='reccomendai.ShopProduct', to='reccomendai.shop'),
        ),
        migrations.CreateModel(
            name='ChequeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('cheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reccomendai.cheque')),
                ('shop_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reccomendai.shopproduct')),
            ],
        ),
        migrations.AddField(
            model_name='cheque',
            name='products',
            field=models.ManyToManyField(through='reccomendai.ChequeProduct', to='reccomendai.shopproduct'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reccomendai.shop'),
        ),
    ]