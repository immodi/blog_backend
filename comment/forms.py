from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=999)
    content = forms.CharField(max_length=9999999)
    post_id = forms.IntegerField()