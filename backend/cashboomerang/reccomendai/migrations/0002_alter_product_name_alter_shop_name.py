# Generated by Django 4.0.6 on 2022-07-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reccomendai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
