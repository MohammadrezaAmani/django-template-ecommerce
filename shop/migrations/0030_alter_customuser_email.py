# Generated by Django 3.2.9 on 2021-12-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0029_auto_20211220_2036"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
