# Generated by Django 3.2.9 on 2021-12-20 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20211217_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myshop',
            name='image_head2',
        ),
        migrations.RemoveField(
            model_name='myshop',
            name='image_head3',
        ),
    ]
