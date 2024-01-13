from django import forms
from django.contrib.auth.forms import UserCreationForm

from shop.models import (
    Comment,
    Comment_shop,
    CustomUser,
    Product,
    contact_with_us,
    myshop,
    postinfo,
    ticket,
    wishlist,
)


class wishliststatus(forms.ModelForm):
    class Meta:
        model = wishlist
        fields = ["status"]


class postform(forms.ModelForm):
    class Meta:
        model = postinfo
        exclude = ["user", "time_add"]


class Contact(forms.ModelForm):
    class Meta:
        model = contact_with_us
        fields = ["content", "name"]


class ChangeProfile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]


class RegisterTicket(forms.ModelForm):
    class Meta:
        model = ticket
        exclude = ["user", "is_answerd", "date_posted", "answer"]


class Updateshop(forms.ModelForm):
    class Meta:
        model = myshop
        exclude = ["products", "h_index", "owner", "slug", "grade", "stars"]


class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = myshop
        exclude = ["products", "owner", "h_index", "grade", "stars", "stars_left"]


class ShopComment(forms.ModelForm):
    class Meta:
        model = Comment_shop
        fields = ("grade", "content")


class UserShop(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["shop", "username"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ["username", "email"]


class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "phone", "password1", "password2"]


class UpdateWishlist(forms.ModelForm):
    class Meta:
        model = wishlist
        exclude = ["buyer", "product", "paid", "time_add", " post_info", "status"]


class Wishlist(forms.ModelForm):
    class Meta:
        model = wishlist
        exclude = [
            "buyer",
            "product",
            "paid",
            "time_add",
            "shop",
            "post_info",
            "status",
        ]


class Updateproduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["user", "count_out_stock", "stars"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("grade", "content")


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "user",
            "inventory",
            "count_out_stock",
            "stars",
            "stars_left",
            "star_rate",
        ]
