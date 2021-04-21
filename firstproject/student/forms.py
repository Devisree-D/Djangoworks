from django import forms

class StudentRegistrationform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'box'}))
    course=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))



class Studentloginpage(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'box'}))

    def clean(self):
        print("valid")
