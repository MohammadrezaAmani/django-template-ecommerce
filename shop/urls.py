from django.urls import path

from . import views

urlpatterns = [
    path("", views.shop, name="shop"),
    path("product/<int:pk>", views.product_details, name="product-details"),
    path("all_products/", views.all_products, name="all_products"),
    # path('shop_search/', views.shop_search, name='shop_search'),
    # path('all_products/', views.all_products, name='all_products'),
    # path('update_product/<int:pk>', views.update_product, name='update_product'),
    # path('update_shop/', views.update_shop, name='update_shop'),
    # path('category/<int:category_id>', views.category_shop, name='category_shop'),
]
