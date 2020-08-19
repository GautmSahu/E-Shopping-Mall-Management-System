"""Shopping_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Shopping_Site import settings
from e_mall import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('admin_login/',views.admin_login,name="admin_login"),
path('admin_verify/',views.admin_verify,name="admin_verify"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_products/',views.admin_products,name="admin_products"),
    path('save_product/',views.save_product,name="save_product"),
    path('register/',views.register,name="register"),
    path('register_user/',views.register_user,name="register_user"),
    path('admin_all_users/',views.admin_all_users,name="admin_all_users"),
    path('admin_see_users/',views.admin_see_users,name="admin_see_users"),
    path('approve_user/',views.approve_user,name="approve_user"),
    path('decline_user/', views.decline_user, name="decline_user"),
    path('admin_update_product/',views.admin_update_product,name="admin_update_product"),
    path('admin_save_product/',views.admin_save_product,name="admin_save_product"),
    path('admin_deactive_product/',views.admin_deactive_product,name="admin_deactive_product"),
    path('user_login/',views.user_login,name="user_login"),
    path('validate_user/',views.validate_user,name="validate_user"),
    path('user_forget_password/',views.user_forget_password,name="user_forget_password"),
    path('user_reset_password/',views.user_reset_password,name="user_reset_password"),
    path('user_main/',views.user_main,name="user_main"),
    path('cart_items/',views.cart_items,name="cart_items"),
    path('save_cart_items/',views.save_cart_items,name="save_cart_items"),
    path('del_cart/',views.del_cart,name="del_cart"),
    path('buyproduct/',views.buyproduct,name="buyproduct"),
    path('place_order/',views.place_order,name="place_order"),
    path('productdetails/',views.productdetails,name="productdetails"),
    path('userorders/',views.userorders,name="userorders"),
    path('userlogout/',views.userlogout,name="userlogout")
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
