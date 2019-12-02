from django.shortcuts import render
from django.http import JsonResponse
from chats.models import Chat
from users.models import User
from members.models import Member
from chats.forms import ChatForm, CreateChatForm
from rest_framework.decorators import api_view
import json


@api_view(['POST'])
def create_chat(request):
    data = json.loads(request.body)
    form = CreateChatForm(data)
    if form.is_valid():
        chat = Chat(topic=data['topic'], is_group_chat=data['is_group_chat'])
        chat.save()
        user = User.objects.get(username=data['username'])
        opponent = User.objects.get(username=data['opponent'])
        member_1 = Member(chat=chat, user=user)
        member_2 = Member(chat=chat, user=opponent)
        member_1.save()
        member_2.save()
        return JsonResponse({
            'success': True,
            'chat ID': [chat.id, member_1.id, member_2.id]
        })
    return JsonResponse({'errors': form.errors}, status=400)


@api_view(['GET'])
def get_all(request):
    user = User.objects.filter(username=request.GET['username']).get()
    chats = Member.objects.filter(user=user)
    result = []
    for chat in chats:
        result.append({
            'opponent': Member.objects.exclude(user=user).get(chat=chat.chat).user.username,
            'chat': {
                'topic': chat.chat.topic,
                'last_message': chat.chat.last_message,
            },
        })
    return JsonResponse({'result': result})

