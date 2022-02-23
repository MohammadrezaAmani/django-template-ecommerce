from django.contrib import admin

from .models import myshop, CustomUser, contact_with_us, Comment_shop, ticket, Category, Comment, Product, wishlist,pakage_shop, Order,SupCategory,postinfo

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