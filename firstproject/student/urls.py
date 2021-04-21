"""firstproject URL Configuration

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

# from student.views import stud_register,student_login,view_timetable,post_feedback,registration,log_in,stud_fb
from django.urls import path
from student.views import registration,stud_delete,loginpage

urlpatterns = [
    path("register/",registration,name="register"),
    path("delete/<int:id>",stud_delete,name="delete"),
    path("log/",loginpage,name="log")
    ]


    # path('register/',stud_register),
    # path('timetable/',view_timetable),
    # path('login/',student_login),
    # path('feedback/',post_feedback),
    # path('signup/',registration,name="signup"),
    # path('logged/',log_in,name="logged"),
    # path('fb/',stud_fb,name="fb")


