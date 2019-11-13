from django import forms
from members.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'new_messages', 'chat', 'last_read_message']

