# Generated by Django 3.2.9 on 2021-12-17 21:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0027_myshop_about"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myshop",
            name="banner_title1",
        ),
        migrations.RemoveField(
            model_name="myshop",
            name="banner_title2",
        ),
        migrations.RemoveField(
            model_name="myshop",
            name="banner_title3",
        ),
        migrations.RemoveField(
            model_name="myshop",
            name="why_us_d1",
        ),
        migrations.RemoveField(
            model_name="myshop",
            name="why_us_d2",
        ),
        migrations.RemoveField(
            model_name="myshop",
            name="why_us_d3",
        ),
    ]
