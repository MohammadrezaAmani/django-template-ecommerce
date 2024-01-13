from django.contrib import admin

from .models import (
    Category,
    Comment,
    Comment_shop,
    CustomUser,
    Order,
    Product,
    SupCategory,
    contact_with_us,
    myshop,
    postinfo,
    ticket,
    wishlist,
)

admin.site.register(postinfo)
admin.site.register(SupCategory)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(wishlist)
admin.site.register(contact_with_us)
admin.site.register(Comment_shop)
admin.site.register(ticket)
admin.site.register(myshop)
admin.site.register(CustomUser)
