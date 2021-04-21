from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookcreateForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            "book_name":forms.TextInput(attrs={'class':'box'}),
            "author":forms.TextInput(attrs={'class':'box'}),
            "price":forms.TextInput(attrs={'class':'box'}),
            "pages":forms.TextInput(attrs={'class':'box'}),
            "category": forms.TextInput(attrs={'class': 'box'})
        }

    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        pages=cleaned_data.get("pages")
        if price<0:
            msg = "invalid price. Pls provide valid value"
            self.add_error("price",msg)
        elif pages<0:
            msg = "invalid page value. Pls provide valid value"
            self.add_error("pages", msg)

class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

# class BookupdateForm(ModelForm):
#     class Meta:
#         model=Book
#         fields='__all__'
#
















# class BookcreateForm(forms.Form):
    # book_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'box'}))
    # author=forms.CharField(widget=forms.TextInput(attrs={'class': 'box'}))
    # price=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'box'}))
    # pages=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'box'}))
    # category=forms.CharField(widget=forms.TextInput(attrs={'class': 'box'}))