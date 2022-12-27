from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()

class SearchUserForm(forms.Form):
    name = forms.CharField()