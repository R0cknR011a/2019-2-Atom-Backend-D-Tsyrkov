from django import forms
from chats.models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'

class CreateChatForm(forms.Form):
    username = forms.CharField(max_length=16)
    opponent = forms.CharField(max_length=16)

