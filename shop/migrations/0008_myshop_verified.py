# Generated by Django 3.2.9 on 2021-11-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_auto_20211120_0141"),
    ]

    operations = [
        migrations.AddField(
            model_name="myshop",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
