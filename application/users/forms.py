from django import forms
from users.models import User

class UserForm(forms.Form):
    fullname = forms.CharField()
    bio = forms.CharField()
    username = forms.CharField()

class UserAvatarForm(forms.Form):
    username = forms.CharField()
    avatar = forms.FileField()
    
