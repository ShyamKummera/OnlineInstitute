from django import forms

class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=5)

