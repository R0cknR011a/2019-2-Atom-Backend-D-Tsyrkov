from django import forms
from chats.models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'

class CreateChatForm(forms.Form):
    topic = forms.CharField(max_length=32)
    username = forms.CharField(max_length=16)
    opponent = forms.CharField(max_length=16)
    is_group_chat = forms.BooleanField(required=False)

