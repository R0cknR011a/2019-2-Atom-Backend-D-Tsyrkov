from django import forms
from attachments.models import Attachment

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['attach_type', 'url', 'chat', 'user']

class AttachmentChatCreateForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['chat']
