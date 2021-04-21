"""Bookproject URL Configuration

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
from Book.views import book_create,book_delete,book_view,book_update,registration,login_view,log_out
from .views import Books,BookCreate,BookUpdate,BookDetail,Bookdelete
urlpatterns = [
    path('create/',book_create,name="create"),
    path('delete/<int:id>',book_delete,name="delete"),
    path('view/<int:id>',book_view,name="view"),
    path('update/<int:id>',book_update,name="update"),
    path('register/',registration,name="register"),
    path('login/',login_view,name="login"),
    path('logout/',log_out,name="out"),
    path('clslist/',Books.as_view(),name="clslist"),
    path("clscreate/",BookCreate.as_view(),name="clscreate"),
    path('clsupdate/<int:pk>',BookUpdate.as_view(),name="clsupdate"),
    path('clsdetail/<int:pk>',BookDetail.as_view(),name="clsdetail"),
    path('clsdelete/<int:pk>',Bookdelete.as_view(),name="clsdelete")





]
