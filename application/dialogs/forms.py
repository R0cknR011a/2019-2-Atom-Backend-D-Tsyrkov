from django import forms
from dialogs.models import Message

class MessageForm(forms.Form):
    username = forms.CharField(max_length=16)
    opponent = forms.CharField(max_length=16)
    content = forms.CharField(required=False)
    date = forms.DateTimeField()
    attach_type = forms.CharField(max_length=16, required=False)

class ReadMessageForm(forms.Form):
    username = forms.CharField(max_length=16)
    opponent = forms.CharField(max_length=16)
    message_key = forms.CharField()
