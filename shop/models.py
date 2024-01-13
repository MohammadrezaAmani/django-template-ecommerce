from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from extensions.utils import jalali_converter


def one_month_from_today():
    return timezone.now() + timedelta(days=30)


choices_my = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="اسم دسته")
    photo = models.ImageField(upload_to="products_category", verbose_name="عکس دسته")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SupCategory(models.Model):
    name = models.CharField(max_length=30, verbose_name="اسم دسته")
    photo = models.ImageField(upload_to="products_category", verbose_name="عکس سر دسته")
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    svg = models.TextField()

    def __str__(self):
        return self.name


class pakage_shop(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=10)
    left = models.BooleanField(default=False)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کالا")
    photo = models.ImageField(upload_to="products", verbose_name="عکس اول کالا")
    photo_2 = models.ImageField(
        upload_to="products", blank=True, verbose_name="عکس دوم کالا"
    )
    photo_3 = models.ImageField(
        upload_to="products", blank=True, verbose_name="عکس سوم کالا"
    )
    photo_4 = models.ImageField(
        upload_to="products", blank=True, verbose_name="عکس چهارم کالا"
    )
    photo_5 = models.ImageField(
        upload_to="products", blank=True, verbose_name="عکس پنجم کالا"
    )
    photo_6 = models.ImageField(
        upload_to="products", blank=True, verbose_name="عکس ششم کالا"
    )
    price = models.IntegerField(verbose_name="قیمت کالا| بدون تخفیف")
    off = models.PositiveIntegerField(verbose_name="تخفیف")
    details = models.TextField(verbose_name="درباره ی کالا")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="دسته ی کالا"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت کالا")
    hot = models.BooleanField(default=False, verbose_name="کالا داغ است؟")
    most_off = models.BooleanField(default=False, verbose_name="کالا پر تخفیف است؟")
    rare = models.BooleanField(default=False, verbose_name="کالا بسیار ویژه است؟")
    in_stock = models.BooleanField(default=True, verbose_name="کالا موجود است؟")
    star_rate = models.PositiveIntegerField(blank=True, default=0)
    stars = models.CharField(default=0, max_length=5)
    stars_left = models.CharField(blank=True, max_length=5)

    def last_price(self):
        return (100 - self.off) * self.price / 100

    def price_comma(self):
        return f"{self.price:,}"

    def last_comma(self):
        lprice = int((100 - self.off) * self.price / 100)
        return f"{lprice:,}"

    def __str__(self):
        return self.name


class myshop(models.Model):
    products = models.ManyToManyField(Product, blank=True, verbose_name="محصولات")
    title = models.CharField(max_length=30, verbose_name="اسم فروشگاه")
    head_title = models.CharField(max_length=100, verbose_name="عنوان سر تیتر")
    head_description = models.CharField(max_length=80, verbose_name="توضیحات سر تیتر")
    head_link = models.TextField(blank=True, verbose_name="لینک تیتر")
    image_head1 = models.ImageField(upload_to="shops.head", verbose_name="عکس تیتر اول")
    slug = models.SlugField(unique=True, verbose_name="آیدی فروشگاه شما")
    phone = models.CharField(max_length=30, verbose_name="تلفن شما")
    phone_bool = models.BooleanField(
        default=False, verbose_name="تلفن شما نمایش داده شود؟"
    )
    address = models.TextField(verbose_name="آدرس شما")
    address_bool = models.BooleanField(
        default=False, verbose_name="آدرس شما نمایش داده شود؟"
    )
    why_us1 = models.CharField(max_length=50, verbose_name="عنوان اول چرا ما")
    why_us2 = models.CharField(max_length=50, verbose_name="عنوان دوم چرا ما")
    why_us3 = models.CharField(max_length=50, verbose_name="عنوان سوم چرا ما")
    image_banner1 = models.ImageField(
        upload_to="shops.banner", verbose_name="عکس بنر اول"
    )
    image_banner2 = models.ImageField(
        upload_to="shops.banner", verbose_name="عکس بنر دوم"
    )
    image_banner3 = models.ImageField(
        upload_to="shops.banner", verbose_name="عکس بنر سوم"
    )
    image_look = models.ImageField(upload_to="shops.look", verbose_name="عکس پوستر")
    title_look = models.CharField(max_length=50, verbose_name="عنوان پوستر")
    description_look = models.TextField(verbose_name="توضیحات پوستر")
    h_index = models.IntegerField(default=0, verbose_name="رتبه ی فروشگاه")
    grade = models.PositiveIntegerField(default=0, verbose_name="رتبه بر اساس نظرات")
    stars = models.CharField(default=0, max_length=5)
    stars_left = models.CharField(blank=True, max_length=5)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    time_created = models.DateTimeField(
        default=timezone.now, blank=True, verbose_name="زمان ساخت فروشگاه"
    )
    time_end = models.DateTimeField(
        default=one_month_from_today, blank=True, verbose_name="زمان پایان اشتراک"
    )
    seller_info = models.CharField(
        max_length=150,
        verbose_name="مشتری از کجا محصول شما رو خریداری کند؟(برای تمام محصولات اعمال میشود)",
    )
    about = models.TextField(verbose_name="درباره ی فروشگاه")

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11)
    phone_active = models.BooleanField(default=False)
    shop = models.OneToOneField(myshop, blank=True, on_delete=models.CASCADE, null=True)
    owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Comment(models.Model):
    feedbacker = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="ارسال کننده ی نظر",
    )
    content = models.TextField(verbose_name="محتوای کامنت")
    date_posted = models.DateTimeField(
        default=timezone.now, verbose_name="زمان ارسال کامنت"
    )
    grade = models.PositiveIntegerField(choices=choices_my, verbose_name="امتیاز")
    stars = models.CharField(default=0, max_length=5)
    stars_left = models.CharField(blank=True, max_length=5)
    products = models.ManyToManyField(Product, blank=True, verbose_name="کالا")

    def jpublish(self):
        return jalali_converter(self.date_posted)


class contact_with_us(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.user.username + " " + self.name


class Comment_shop(models.Model):
    feedbacker = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="نظر دهنده",
    )
    content = models.TextField(verbose_name="محتوای کامنت")
    date_posted = models.DateTimeField(
        default=timezone.now, verbose_name="زمان پست کامنت"
    )
    grade = models.PositiveIntegerField(choices=choices_my, verbose_name="امتیاز کامنت")
    stars = models.CharField(default=0, max_length=5)
    stars_left = models.CharField(blank=True, max_length=5)
    shop = models.ManyToManyField(myshop, blank=True)

    def jpublish(self):
        return jalali_converter(self.date_posted)


class ticket(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان تیکت")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.TextField(verbose_name="سوال شما")
    answer = models.TextField(blank=True)
    is_answerd = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def jpublish(self):
        return jalali_converter(self.date_posted)

    def __str__(self):
        return self.user.username + " " + self.title


class postinfo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    address = models.TextField()
    postal_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    time_add = models.DateTimeField(default=timezone.now, verbose_name="زمان اضافه شدن")


choices_post = (
    ("کالا در حال آماده سازی برای ارسال است", "کالا در حال آماده سازی برای ارسال است"),
    ("کالا تحویل پست داده شد", "کالا تحویل پست داده شد"),
)


class wishlist(models.Model):
    post_info = models.ForeignKey(
        postinfo,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="اطلاعات ارسال",
    )
    shop = models.ForeignKey(
        myshop, on_delete=models.CASCADE, verbose_name="نام فروشگاه"
    )
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="نام محصول"
    )
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")
    time_add = models.DateTimeField(default=timezone.now, verbose_name="زمان اضافه شدن")
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=choices_post,
        verbose_name="وضعیت ارسال کالا",
    )

    def __str__(self):
        return self.buyer.username + str(self.shop)


class Order(models.Model):
    grade = models.PositiveIntegerField(choices=choices_my)
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.owner)
