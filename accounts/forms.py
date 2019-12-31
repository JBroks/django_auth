from django import forms


class UserLoginForm(forms.Form):
    """Forms to be used to lo users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)