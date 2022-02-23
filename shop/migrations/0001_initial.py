# Generated by Django 3.2.9 on 2021-11-19 17:06

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='myshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='اسم فروشگاه')),
                ('head1', models.CharField(max_length=100, verbose_name='سر تیتر')),
                ('head2', models.CharField(max_length=100, verbose_name='عنوان دوم')),
                ('head3', models.CharField(max_length=100, verbose_name='عنوان سوم')),
                ('head_title', models.CharField(max_length=100, verbose_name='عنوان سر تیتر')),
                ('head_description', models.CharField(max_length=80, verbose_name='توضیحات سر تیتر')),
                ('head_link', models.TextField(verbose_name='لینک تیتر')),
                ('link_name', models.CharField(max_length=80, verbose_name='نام لینک')),
                ('image_head1', models.ImageField(upload_to='shops.head', verbose_name='عکس تیتر اول')),
                ('image_head2', models.ImageField(upload_to='shops.head', verbose_name='عکس تیتر دوم')),
                ('image_head3', models.ImageField(upload_to='shops.head', verbose_name='عکس تیتر سوم')),
                ('slug', models.SlugField(unique=True, verbose_name='آیدی فروشگاه شما')),
                ('phone', models.CharField(max_length=30, verbose_name='تلفن شما')),
                ('phone_bool', models.BooleanField(default=False, verbose_name='تلفن شما نمایش داده شود؟')),
                ('address', models.TextField(verbose_name='آدرس شما')),
                ('address_bool', models.BooleanField(default=False, verbose_name='آدرس شما نمایش داده شود؟')),
                ('why_us1', models.CharField(max_length=50, verbose_name='عنوان اول چرا ما')),
                ('why_us_d1', models.CharField(max_length=50, verbose_name='محتوا اول چرا ما')),
                ('why_us2', models.CharField(max_length=50, verbose_name='عنوان دوم چرا ما')),
                ('why_us_d2', models.CharField(max_length=50, verbose_name='محتوا دوم چرا ما')),
                ('why_us3', models.CharField(max_length=50, verbose_name='عنوان سوم چرا ما')),
                ('why_us_d3', models.CharField(max_length=50, verbose_name='محتوا سوم چرا ما')),
                ('image_banner1', models.ImageField(upload_to='shops.banner', verbose_name='عکس بنر اول')),
                ('image_banner2', models.ImageField(upload_to='shops.banner', verbose_name='عکس بنر دوم')),
                ('image_banner3', models.ImageField(upload_to='shops.banner', verbose_name='عکس بنر سوم')),
                ('about_content', models.TextField(verbose_name='درباره ی فروشگاه')),
                ('h_index', models.IntegerField(default=0, verbose_name='رتبه ی فروشگاه')),
                ('why_us', models.TextField(verbose_name='چرا ما؟')),
                ('grade', models.PositiveIntegerField(default=0, verbose_name='رتبه بر اساس نظرات')),
                ('stars', models.CharField(default=0, max_length=5)),
                ('stars_left', models.CharField(blank=True, max_length=5)),
                ('time_created', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='زمان ساخت فروشگاه')),
                ('is_active', models.BooleanField(default=True)),
                ('seller_info', models.CharField(max_length=150, verbose_name='مشتری از کجا محصول شما رو خریداری کند؟(برای تمام محصولات اعمال میشود)')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('shop', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.myshop')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]