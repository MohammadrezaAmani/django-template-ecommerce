# Generated by Django 3.2.9 on 2021-12-11 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0019_postinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="post_info",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.postinfo",
                verbose_name="اطلاعات ارسال",
            ),
            preserve_default=False,
        ),
    ]
