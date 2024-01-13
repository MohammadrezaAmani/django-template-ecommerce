import math
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from blog.forms import (
    Comment_shop,
    CommentForm,
    ProductCreateForm,
    ShopComment,
    ShopCreateForm,
    Updateproduct,
    Updateshop,
    Wishlist,
    postform,
    wishliststatus,
)

from .models import (
    Category,
    Comment,
    CustomUser,
    Order,
    Product,
    SupCategory,
    myshop,
    postinfo,
    wishlist,
)


def one_month_from_today():
    return timezone.now() + timedelta(days=30)


def three_month_from_today():
    return timezone.now() + timedelta(days=90)


def six_month_from_today():
    return timezone.now() + timedelta(days=183)


def one_year_from_today():
    return timezone.now() + timedelta(days=365)


def help(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    if request.user.is_anonymous:
        is_owner = ""
        context = {
            "scategory": SupCategory.objects.all(),
            "wish": 0,
            "shop": shop,
            "is_owner": is_owner,
        }
    else:
        if request.user.is_anonymous:
            login = False

        else:
            login = True
            if request.user.owner:
                owner = True
                me = CustomUser.objects.get(username=request.user.username)
                my_shop = me.shop
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "my_shop": my_shop,
                    "owner": owner,
                }
            else:
                owner = False
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "owner": owner,
                }

    return render(request, "blog/help.html", context)


def all_products(request, slug):
    shop = myshop.objects.get(slug=slug)
    products = shop.products.all()

    if request.user.is_anonymous:
        login = False
        owner = False
        context = {
            "shop": shop,
            "products": products,
            "login": login,
            "scategory": SupCategory.objects.all(),
        }
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "shop": shop,
                "products": products,
                "login": login,
                "my_shop": my_shop,
                "owner": owner,
                "scategory": SupCategory.objects.all(),
            }
        else:
            owner = False
            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "shop": shop,
                "products": products,
                "login": login,
                "owner": owner,
                "scategory": SupCategory.objects.all(),
            }

    return render(request, "shop/all_products.html", context)


def shop(request, slug):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    shop = myshop.objects.get(slug=slug)

    comments = Comment_shop.objects.filter(shop=shop).order_by("-date_posted")
    score = 0
    for i in range(0, len(comments)):
        score += int(comments[i].grade)
    if len(comments) != 0:
        final_score = score / len(comments)
    else:
        final_score = 0

    shop.grade = final_score
    final_score = math.ceil(final_score)
    shop.stars = final_score * "1"
    shop.stars_left = (5 - final_score) * "1"
    shop.save()

    products_shop = shop.products.filter().order_by("-date")[0:8]
    rare = shop.products.filter(rare=True)[0:3]
    off = shop.products.filter(most_off=True)[0:3]
    hot = shop.products.filter(hot=True)[0:3]

    shop_m = [
        shop,
    ]
    if request.method == "POST":
        form = ShopComment(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.feedbacker = request.user
            obj.save()
            obj.shop.set(shop_m)
            obj.save()
            obj.stars = obj.grade * "1"
            obj.save()
            obj.stars_left = (5 - obj.grade) * "1"
            obj.save()
            return redirect("shop", shop.slug)
    else:
        form = ShopComment()

    if request.user.is_anonymous:
        add_comment = False
    else:
        comments_me = comments.filter(feedbacker=request.user)
        j = 0
        for i in comments_me:
            j += 1

        if j > 3:
            add_comment = False
        else:
            add_comment = True

    comments = comments[0:10]

    if request.user.is_anonymous:
        context = {
            "products": products_shop,
            "login": login,
            "add_comment": add_comment,
            "comments": comments,
            "shop": shop,
            "form": form,
            "rare": rare,
            "hot": hot,
            "off": off,
            "scategory": SupCategory.objects.all(),
        }
    else:
        if request.user.owner:
            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "products": products_shop,
                "login": login,
                "my_shop": my_shop,
                "owner": owner,
                "add_comment": add_comment,
                "comments": comments,
                "shop": shop,
                "form": form,
                "rare": rare,
                "hot": hot,
                "off": off,
                "scategory": SupCategory.objects.all(),
            }
        else:
            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "products": products_shop,
                "login": login,
                "add_comment": add_comment,
                "comments": comments,
                "shop": shop,
                "form": form,
                "rare": rare,
                "scategory": SupCategory.objects.all(),
                "hot": hot,
                "off": off,
            }

    return render(request, "shop/shop.html", context)


@login_required
def update_shop(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False
            return redirect("add_shop")

    me = CustomUser.objects.get(username=request.user.username)
    my_shop = me.shop
    shop = my_shop

    if request.user == request.user:
        if request.method == "POST":
            form = Updateshop(request.POST, request.FILES, instance=shop)

            if form.is_valid():
                # os.remove(os.path.join('', image_path))
                obj = form.save(commit=False)
                obj.save()
                return redirect("shop", shop.slug)
        else:
            form = Updateshop(instance=shop)

        context = {
            "scategory": SupCategory.objects.all(),
            "wish": wishlist.objects.filter(buyer=request.user)
            .filter(paid=False)
            .__len__(),
            "login": login,
            "my_shop": my_shop,
            "owner": owner,
            "shop": shop,
            "form": form,
        }
        return render(request, "shop/update_shop.html", context)


@login_required
def add_shop(request):
    if request.method == "POST":
        form1 = ShopCreateForm(request.POST, request.FILES)
        user = request.user
        print(form1.errors)
        #
        # print('obj.slug1')

        if form1.is_valid():
            # print('obj.slug2')

            obj = form1.save(commit=False)
            # obj.owner = request.user
            # user.shop = obj
            # user.save()
            # print('obj.slug3')
            shop_slug = obj.slug
            # print(obj.slug)
            # product_pk = obj.pk
            # user.shop = obj
            # print(obj)
            # print('obj.slug4')

            # print(user)
            # CustomUser.objects.create(shop=obj)
            obj.save()
            # print('obj.slug5')

            # print(form1)
            shop_o = myshop.objects.get(slug=shop_slug)
            # print('obj.slug16')

            user.shop = shop_o
            user.owner = True
            # print('obj.slug7')

            user.save()
            # print('obj.slug8')

            return redirect("home")
    else:
        form1 = ShopCreateForm()

    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
            context = {
                "scategory": SupCategory.objects.all(),
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "login": login,
                "my_shop": my_shop,
                "owner": owner,
                "form": form1,
                # 'is_owner': is_owner,
            }
        else:
            owner = False
            context = {
                "scategory": SupCategory.objects.all(),
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "login": login,
                "owner": owner,
                "form": form1,
                # 'is_owner': is_owner,
            }

    return render(request, "shop/add_shop.html", context)


@login_required
def update_product(request, pk):
    # if request.user.is_anonymous:
    #     pass
    # elif myshop.objects.filter(owner=request.user).exists():
    #     pass
    # else:
    #     return redirect('add_shop')
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False
            return redirect("add_shop")

    me = CustomUser.objects.get(username=request.user.username)
    my_shop = me.shop
    shop = my_shop

    products = shop.products.all()
    if request.user.owner:
        is_owner = True
    else:
        is_owner = False

    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        form = Updateproduct(request.POST, request.FILES, instance=product)

        if form.is_valid():
            # os.remove(os.path.join('', image_path))
            form.save()
            return redirect("shop", shop.slug)

    else:
        form = Updateproduct(instance=product)

    context = {
        "scategory": SupCategory.objects.all(),
        "wish": wishlist.objects.filter(buyer=request.user)
        .filter(paid=False)
        .__len__(),
        "shop": shop,
        "form": form,
        "is_owner": is_owner,
        "products": products,
        "login": login,
        "my_shop": my_shop,
        "owner": owner,
    }

    return render(request, "shop/update_product.html", context)


@login_required
def add_product(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False
            return redirect("add_shop")

    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            # os.remove(os.path.join('', image_path))
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # shop_owner = myshop.objects.get(owner=request.user)
            request.user.shop.products.add(obj)
            return redirect("shop", request.user.shop.slug)
    else:
        form = ProductCreateForm()

    context = {
        "scategory": SupCategory.objects.all(),
        "wish": wishlist.objects.filter(buyer=request.user)
        .filter(paid=False)
        .__len__(),
        "form": form,
        "shop": request.user.shop,
        "login": login,
        "my_shop": my_shop,
        "owner": owner,
        # 'is_owner': is_owner,
    }
    return render(request, "shop/add_product.html", context)


@login_required
def active_shop(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False
            return redirect("add_shop")

    if request.method == "POST":
        Order.objects.filter(owner=request.user).delete()

        if request.POST["action"] == "1":
            my_order = Order.objects.create(grade=1, owner=request.user)
            my_order.save()
            return redirect("go-to-gateway")
        elif request.POST["action"] == "2":
            my_order = Order.objects.create(grade=2, owner=request.user)
            my_order.save()
            return redirect("go-to-gateway")
        elif request.POST["action"] == "3":
            my_order = Order.objects.create(grade=3, owner=request.user)
            my_order.save()
            return redirect("go-to-gateway")
        elif request.POST["action"] == "4":
            my_order = Order.objects.create(grade=4, owner=request.user)
            my_order.save()
            return redirect("go-to-gateway")
    # # all = 1
    # # for i in range(0,50):
    # #     all = all*(365-i)/365
    # # print(all)
    # # shop = myshop.objects.get(owner=request.user)
    # # pakage_shop_m = pakage_shop.objects.all()
    # # if requestall*(365-i)/365
    # # print(all)
    # # shop = mysho.time_end = one_year_from_today()
    # #         # myshop.objects.get(owner=request.user).update(time_end='some value')
    # #         shop.save()
    # #     elif request.POST['action']=="90000":
    # #         shop.time_end = six_month_from_today()
    # #         shop.save()
    # #     elif request.POST['action'] == "40000":
    # #         shop.time_end = three_month_from_today()
    # #         shop.save()
    # #     elif request.POST['action'] == "25000":
    # #         shop.time_end = one_month_from_today()
    # #         shop.save()

    # #     shop = myshop.objects.get(owner=request.user)
    # #     # print(request)
    # #     print(request.POST)
    # #     print(request.POST['action'])

    # # pakage_shop_l = pakage_shop.objects.filter(left=True)
    # # pakage_shop_r = pakage_shop.objects.filter(left=False)
    context = {
        "wish": wishlist.objects.filter(buyer=request.user)
        .filter(paid=False)
        .__len__(),
        "scategory": SupCategory.objects.all(),
    }

    return render(request, "blog/active_shop.html", context)


def product_details(request, slug, pk):
    shop = myshop.objects.get(slug=slug)
    own = False
    if request.user.is_anonymous:
        login = False
        wish_op = 0
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop

            if my_shop.pk == shop.pk:
                own = True
            wish_op = wishlist.objects.filter(buyer=request.user).__len__()
        else:
            owner = False
            wish_op = wishlist.objects.filter(buyer=request.user).__len__()

    # if request.user == shop.owner:
    #     is_owner = True
    # else:
    #     is_owner = False

    product_details = shop.products.get(pk=pk)
    comments = Comment.objects.filter(products=product_details).order_by("-date_posted")

    score = 0
    for i in range(0, len(comments)):
        score += int(comments[i].grade)
    if len(comments) != 0:
        final_score = score / len(comments)
    else:
        final_score = 0

    product_details.star_rate = final_score
    final_score = math.ceil(final_score)
    product_details.stars = final_score * "1"
    product_details.stars_left = (5 - final_score) * "1"
    product_details.save()

    data = {
        "fields1": request.user,
        "fields5": product_details,
    }
    products = [
        product_details,
    ]
    if request.method == "POST":
        if request.POST["action"] == "comment":
            form1 = CommentForm(request.POST)
            form2 = Wishlist()
            if form1.is_valid():
                obj = form1.save(commit=False)
                obj.feedbacker = request.user
                obj.save()
                obj.products.set(products)
                obj.save()
                obj.stars = obj.grade * "1"
                obj.save()
                obj.stars_left = (5 - obj.grade) * "1"
                obj.save()

                return redirect("product-details", slug, pk)
        elif request.POST["action"] == "add_cart":
            form2 = Wishlist(request.POST)
            form1 = CommentForm()
            if form2.is_valid():
                obj = form2.save(commit=False)
                obj.shop = shop
                obj.buyer = request.user
                obj.product = product_details
                obj.save()
                return redirect("product-details", slug, pk)

        elif request.POST["action"] == "change":
            form1 = CommentForm()
            form2 = Wishlist()
            return redirect("update_product", pk)

        elif request.POST["action"] == "delete":
            form1 = CommentForm()
            form2 = Wishlist()
            if my_shop.pk == shop.pk:
                my_shop.products.get(pk=pk).delete()
                return redirect("shop", slug)

    else:
        form1 = CommentForm()
        form2 = Wishlist()

    score_list = [None] * math.ceil(final_score)
    left_list = [None] * (5 - math.ceil(final_score))
    final_score = math.ceil(final_score)

    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)[0:4]

    if request.user.is_anonymous:
        add_comment = False
    else:
        comments_me = comments.filter(feedbacker=request.user)
        j = 0
        for i in comments_me:
            j += 1

        if j > 3:
            add_comment = False
        else:
            add_comment = True
    num_photos = 0
    if product_details.photo_3:
        num_photos += 1
    if product_details.photo_4:
        num_photos += 1
    if product_details.photo_5:
        num_photos += 1
    if product_details.photo_6:
        num_photos += 1

    any = True
    if request.user.is_anonymous:
        any = False

    if request.user.is_anonymous:
        context = {
            "wish": wish_op,
            "scategory": SupCategory.objects.all(),
            "login": login,
            "any": any,
            "now": timezone.now,
            "num_photos": num_photos,
            "product": product_details,
            "related_products": related_products,
            "comments": comments,
            "form": form1,
            "form2": form2,
            "final_score": final_score,
            "score_list": score_list,
            "left_list": left_list,
            # 'is_owner': is_owner,
            "shop": shop,
            "add_comment": add_comment,
        }
    else:
        if request.user.owner:
            context = {
                "scategory": SupCategory.objects.all(),
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "own": own,
                "my_products": my_shop.products.all(),
                "login": login,
                "my_shop": my_shop,
                "owner": owner,
                "any": any,
                "now": timezone.now,
                "num_photos": num_photos,
                "product": product_details,
                "related_products": related_products,
                "comments": comments,
                "form": form1,
                "form2": form2,
                "final_score": final_score,
                "score_list": score_list,
                "left_list": left_list,
                # 'is_owner': is_owner,
                "shop": shop,
                "add_comment": add_comment,
            }
        else:
            context = {
                "scategory": SupCategory.objects.all(),
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "own": own,
                "login": login,
                "owner": owner,
                "any": any,
                "now": timezone.now,
                "num_photos": num_photos,
                "product": product_details,
                "related_products": related_products,
                "comments": comments,
                "form": form1,
                "form2": form2,
                "final_score": final_score,
                "score_list": score_list,
                "left_list": left_list,
                # 'is_owner': is_owner,
                "shop": shop,
                "add_comment": add_comment,
            }

    return render(request, "shop/product-details.html", context)


@login_required
def cart(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    wishlist_p = 0
    shop = myshop.objects.all()

    if request.method == "POST":
        pk = request.POST["action"]
        wishlist_o = wishlist.objects.filter(pk=pk)
        wishlist_o.delete()

    if request.user.is_anonymous:
        is_owner = ""
        context = {
            "scategory": SupCategory.objects.all(),
            "wish": wishlist.objects.filter(buyer=request.user)
            .filter(paid=False)
            .__len__(),
            "shop": shop,
            "is_owner": is_owner,
            "wish_list": wishlist_p,
        }
    else:
        # shop = myshop.objects.get(owner=request.user)
        wishlist_all = wishlist.objects.filter(buyer=request.user).filter(paid=False)
        all = 0
        post = 0
        off = 0
        op = 0
        for i in wishlist_all:
            wishlist_p += 1
            all += i.product.last_price()
            op += i.product.price

        shop_owner = request.user.shop
        # if shop_owner:
        #     is_owner = True
        #     owner_name = request.user.username
        #     shop = myshop.objects.get(owner=request.user)
        # else:
        #     is_owner = False
        all_all = int(all + post)
        off = op - all
        off = off * 10000
        off = (int)(off / 100)
        off = off / 100
        op = int(op)

        if request.user.is_anonymous:
            login = False

        else:
            login = True
            if request.user.owner:
                owner = True
                me = CustomUser.objects.get(username=request.user.username)
                my_shop = me.shop
                context = {
                    "scategory": SupCategory.objects.all(),
                    "off": f"{off:,}",
                    "all_all": f"{all_all:,}",
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "my_shop": my_shop,
                    "owner": owner,
                    "all_price": f"{op:,}",
                    # 'shop': shop,
                    # 'owner_name': owner_name,
                    # 'is_owner': is_owner,
                    "wish_list": wishlist_p,
                    "wish_all": wishlist_all,
                }
            else:
                owner = False
                context = {
                    "scategory": SupCategory.objects.all(),
                    "off": f"{off:,}",
                    "all_all": f"{all_all:,}",
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "owner": owner,
                    "all_price": f"{op:,}",
                    # 'shop': shop,
                    # 'owner_name': owner_name,
                    # 'is_owner': is_owner,
                    "wish_list": wishlist_p,
                    "wish_all": wishlist_all,
                }

    return render(request, "blog/cart.html", context)


@login_required
def bought(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    wishlist_all = (
        wishlist.objects.filter(buyer=request.user)
        .filter(paid=True)
        .order_by("-time_add")
    )

    if request.user.is_anonymous:
        is_owner = ""
        context = {
            "scategory": SupCategory.objects.all(),
            "wish": 0,
            "shop": shop,
            "is_owner": is_owner,
            "buy": wishlist_all,
        }
    else:
        if request.user.is_anonymous:
            login = False

        else:
            login = True
            if request.user.owner:
                owner = True
                me = CustomUser.objects.get(username=request.user.username)
                my_shop = me.shop
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "my_shop": my_shop,
                    "owner": owner,
                    "buy": wishlist_all,
                }
            else:
                owner = False
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "owner": owner,
                    "buy": wishlist_all,
                }

    return render(request, "blog/bought.html", context)


@login_required
def sold(request):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    wish_sold = (
        wishlist.objects.filter(shop=my_shop).filter(paid=True).order_by("-time_add")
    )

    if request.user.is_anonymous:
        is_owner = ""
        context = {
            "scategory": SupCategory.objects.all(),
            "wish": wishlist.objects.filter(buyer=request.user)
            .filter(paid=False)
            .__len__(),
            "shop": shop,
            "is_owner": is_owner,
            "sold": wish_sold,
        }
    else:
        shop_owner = request.user.shop

        if request.user.is_anonymous:
            login = False

        else:
            login = True
            if request.user.owner:
                owner = True
                me = CustomUser.objects.get(username=request.user.username)
                my_shop = me.shop
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "my_shop": my_shop,
                    "owner": owner,
                    "sold": wish_sold,
                }
            else:
                owner = False
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "owner": owner,
                    "sold": wish_sold,
                }

    return render(request, "blog/sold.html", context)


@login_required
def sold_detail(request, pk):
    if request.user.is_anonymous:
        login = False
    else:
        login = True
        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop
        else:
            owner = False

    wish_sold = wishlist.objects.filter(shop=my_shop)
    wish_sold = wish_sold.get(pk=pk)
    if request.method == "POST":
        form = wishliststatus(request.POST, instance=wish_sold)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("sold-detail", pk)
    else:
        form = wishliststatus(instance=wish_sold)

    if request.user.is_anonymous:
        is_owner = ""
        context = {
            "scategory": SupCategory.objects.all(),
            "wish": wishlist.objects.filter(buyer=request.user)
            .filter(paid=False)
            .__len__(),
            "shop": shop,
            "is_owner": is_owner,
            "sold": wish_sold,
        }
    else:
        shop_owner = request.user.shop

        if request.user.is_anonymous:
            login = False

        else:
            login = True
            if request.user.owner:
                owner = True
                me = CustomUser.objects.get(username=request.user.username)
                my_shop = me.shop
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "my_shop": my_shop,
                    "owner": owner,
                    "sold": wish_sold,
                    "form": form,
                }
            else:
                owner = False
                context = {
                    "scategory": SupCategory.objects.all(),
                    "wish": wishlist.objects.filter(buyer=request.user)
                    .filter(paid=False)
                    .__len__(),
                    "login": login,
                    "owner": owner,
                    "sold": wish_sold,
                    "form": form,
                }

    return render(request, "blog/sold_detail.html", context)


@login_required
def post_info(request):
    wish_me = wishlist.objects.filter(buyer=request.user).filter(paid=False)
    post_m = postinfo.objects.filter(user=request.user).order_by("-time_add").first()
    if request.method == "POST":
        form = postform(request.POST, instance=post_m)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            for x in wish_me:
                x.post_info = obj
                x.save()

            return redirect("go-to-shop")
    else:
        form = postform(instance=post_m)

    if request.user.is_anonymous:
        login = False
        wish_op = 0

        context = {
            "wish": wishlist.objects.filter(buyer=request.user)
            .filter(paid=False)
            .__len__(),
            "login": login,
            "scategory": SupCategory.objects.all(),
            "form": form,
        }
    else:
        login = True

        if request.user.owner:
            owner = True
            me = CustomUser.objects.get(username=request.user.username)
            my_shop = me.shop

            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "login": login,
                "my_shop": my_shop,
                "owner": owner,
                "form": form,
                "scategory": SupCategory.objects.all(),
            }

        else:
            owner = False

            context = {
                "wish": wishlist.objects.filter(buyer=request.user)
                .filter(paid=False)
                .__len__(),
                "login": login,
                "scategory": SupCategory.objects.all(),
                "owner": owner,
                "form": form,
            }

    return render(request, "blog/post_info.html", context)


def page_404(request, exception):
    return render(request, "404.html", status=404)


def page_403(request, exception):
    return render(request, "403.html", status=403)


def page_500(request, exception):
    return render(request, "500.html", status=500)


def page_400(request, exception):
    return render(request, "400.html", status=400)
