from django .forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Brands,Mobile,Myorders


class BrandcreateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'


class MobilecreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class UserpurchaseForm(ModelForm):
    # items=forms.CharField(max_length=120)
    class Meta:
        model=Myorders
        fields=["items","address","user"]

