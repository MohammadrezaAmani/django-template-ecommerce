# Generated by Django 3.2.6 on 2021-11-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0009_auto_20211121_1219"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo_2",
            field=models.ImageField(
                blank=True, upload_to="products", verbose_name="عکس دوم کالا"
            ),
        ),
    ]
