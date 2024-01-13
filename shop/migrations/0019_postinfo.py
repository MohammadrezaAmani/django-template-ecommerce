# Generated by Django 3.2.9 on 2021-12-11 16:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0018_supcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="postinfo",
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
                ("name", models.CharField(max_length=200)),
                ("family_name", models.CharField(max_length=200)),
                ("address", models.TextField()),
                ("postal_code", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
