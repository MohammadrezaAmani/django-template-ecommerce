# Generated by Django 3.2.9 on 2021-12-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0017_alter_order_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="SupCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="اسم دسته")),
                (
                    "photo",
                    models.ImageField(
                        upload_to="products_category", verbose_name="عکس سر دسته"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("svg", models.TextField()),
                ("categories", models.ManyToManyField(to="shop.Category")),
            ],
        ),
    ]
