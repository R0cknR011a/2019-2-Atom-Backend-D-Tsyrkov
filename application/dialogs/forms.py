from django import forms
from dialogs.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'added_at', 'user', 'chat']

