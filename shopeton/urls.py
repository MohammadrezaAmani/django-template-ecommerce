"""shopeton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from blog.views import home, contact, my_tickets, profile, register, one_product, search, about_us, category,go_to_gateway_view,callback_gateway_view, supcategory, go_to_gateway_shop,callback_gateway_shop
from shop.views import shop, add_shop, update_shop, cart, add_product, update_shop, update_product ,active_shop, post_info, bought, sold, sold_detail, help

from azbankgateways.urls import az_bank_gateways_urls
admin.autodiscover()

urlpatterns = [
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view, name='go-to-gateway'),
    path('go-to-shop/', go_to_gateway_shop, name='go-to-shop'),
    path('callback-gateway/', callback_gateway_view, name='callback-gateway'),
    path('callback_shop/', callback_gateway_shop, name='callback-shop'),
    path('about/', about_us, name='about'),
    path('search/', search, name='search'),
    path('category/<int:pk>', category, name='category'),
    path('supcategory/<int:pk>', supcategory, name='sup-category'),
        
    path('update_product/<int:pk>', update_product, name='update_product'),
    path('update_shop/', update_shop, name='update_shop'),
    
    path('shop/<slug:slug>/', include('shop.urls')),
    path('one_product/<int:pk>', one_product, name='one_product'),
    path('cart/', cart, name='cart'),
    path('help/', help, name='help'),
    path('bought/', bought, name='bought'),
    path('sold/', sold, name='sold'),
    path('sold/<int:pk>', sold_detail, name='sold-detail'),
    path('post_info/', post_info, name='post-info'),
        
    path('addproduct/', add_product, name='add_product'),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('shop/<slug:slug>/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('myticket/', my_tickets, name='my_ticket'),
    path('profile/', profile, name='my_profile'),

    path('active_shop/', active_shop, name='active_shop'),
    path('addshop/', add_shop, name='add_shop'),
    # path('updateshop/<slug:slug>/', update_shop, name='update_shop'),
    # path('search/', user_views.home_search, name='home_search'),

    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('passwordreset_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('passwordreset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('passwordreset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
]

handler404 = "shop.views.page_404"
handler400 = "shop.views.page_400"
# handler500 = "shop.views.page_500"
handler403 = "shop.views.page_403"
handler_404 = "blog.views.page_404"
handler_400 = "blog.views.page_400"
handler_500 = "blog.views.page_500"
handler_403 = "blog.views.page_403"


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)