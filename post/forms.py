from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=999999)
    author = forms.CharField(max_length=255)
