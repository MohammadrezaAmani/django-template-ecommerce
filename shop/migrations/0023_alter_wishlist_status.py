# Generated by Django 3.2.9 on 2021-12-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_wishlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='status',
            field=models.CharField(blank=True, choices=[('کالا در حال آماده سازی برای ارسال است', 'کالا در حال آماده سازی برای ارسال است'), ('کالا تحویل پست داده شد', 'کالا تحویل پست داده شد')], max_length=100, null=True, verbose_name='وضعیت ارسال کالا'),
        ),
    ]
