from django import forms
from users.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'bio']
