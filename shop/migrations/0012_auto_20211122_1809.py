# Generated by Django 3.2.6 on 2021-11-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0011_remove_product_last_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myshop",
            name="banner_title1",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="عنوان بنر اول"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="banner_title2",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="عنوان بنر دوم"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="banner_title3",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="عنوان بنر سوم"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="image_product1",
            field=models.ImageField(
                blank=True, upload_to="shops.product", verbose_name="عکس محصول"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="image_product2",
            field=models.ImageField(
                blank=True, upload_to="shops.product", verbose_name="عکس محصول"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="image_product3",
            field=models.ImageField(
                blank=True, upload_to="shops.product", verbose_name="عکس محصول"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="image_product4",
            field=models.ImageField(
                blank=True, upload_to="shops.product", verbose_name="عکس محصول"
            ),
        ),
        migrations.AlterField(
            model_name="myshop",
            name="image_product5",
            field=models.ImageField(
                blank=True, upload_to="shops.product", verbose_name="عکس محصول"
            ),
        ),
    ]
