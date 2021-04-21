"""MobileApplication URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import brand_view,view_cart,mobile_view,brand_edit,brand_delete,mob_details,mobile_delete,mobile_edit,user_register,user_login,user_logout,feedback,purchase,cart,errorpage,item_delete

urlpatterns = [
    path("listmobiles/",view_cart,name="list"),
    path("brands/",brand_view,name="bnd"),
    path("edit/<int:id>",brand_edit,name="brandedit"),
    path("delete/<int:id>",brand_delete,name="branddelete"),
    path("mobiles/",mobile_view,name="mob"),
    path("detail/<int:id>",mob_details,name="detail"),
    path("mobupdate/<int:id>",mobile_edit,name="mobileupdate"),
    path("mobdelete/<int:id>",mobile_delete,name="mobiledelete"),
    path("register/",user_register,name="register"),
    path("login/",user_login,name="login"),
    path("logout/",user_logout,name="out"),
    path("feedback/",feedback,name="fd"),
    path("purchase/<int:id>",purchase,name="purchase"),
    path("mycart/",cart,name="cart"),
    path("error/",errorpage,name="error"),
    path("itemdelete/<int:id>",item_delete,name="itemdel")

]

# path("",lambda request:render(request,"mobile/mycart.html")),
