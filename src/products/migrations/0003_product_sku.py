# Generated by Django 4.1 on 2022-12-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_discount_price_product_discount_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='123', max_length=50),
            preserve_default=False,
        ),
    ]
