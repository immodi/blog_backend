from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=200, label="username")
    password = forms.CharField(required=True, max_length=200, label="password", widget=forms.PasswordInput())
    email = forms.EmailField(required=True) 
    is_staff = forms.BooleanField(required=False)
    