from django.shortcuts import render
from django.http import JsonResponse
from chats.models import Chat
from users.models import User
from members.models import Member
from dialogs.models import Message
from chats.forms import ChatForm, CreateChatForm
from rest_framework.decorators import api_view
import boto3


@api_view(['POST'])
def create_chat(request):
    form = CreateChatForm(request.POST)
    if form.is_valid():
        chat = Chat(
            topic=request.POST['username'] + ' with ' + request.POST['opponent'],
            is_group_chat=False,
        )
        chat.save()
        user = User.objects.get(username=request.POST['username'])
        opponent = User.objects.get(username=request.POST['opponent'])
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
    user = User.objects.get(username=request.GET['username'])
    chats = Member.objects.filter(user=user)
    result = []
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
        aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
    )
    for chat in chats:
        curr_chat = {}
        opponent = Member.objects.exclude(user=user).get(chat=chat.chat)
        avatar = s3_client.generate_presigned_url('get_object', Params={
                        'Bucket': 'tsyrkov_messanger_bucket',
                        'Key': opponent.user.avatar,
                    }, ExpiresIn=3600)
        curr_chat['avatar'] = avatar
        curr_chat['opponent'] = opponent.user.username
        messages = Message.objects.filter(chat=chat.chat)
        if len(messages) == 0:
            curr_chat['author'] = ''
            curr_chat['last_message'] = ''
            curr_chat['read'] = False
            curr_chat['date'] = ''
        else:
            last_message = messages.last()
            if last_message.user == user:
                if opponent.last_read_message == None:
                    read = False
                else:
                    if last_message.id > opponent.last_read_message.id:
                        read = False
                    else:
                        read = True
            if last_message.user == opponent.user:
                if chat.last_read_message == None:
                    read=False
                else:
                    if last_message.id > chat.last_read_message.id:
                        read = False
                    else:
                        read = True
            curr_chat['author'] = last_message.user.username
            curr_chat['last_message'] = chat.chat.last_message
            curr_chat['read'] = read
            curr_chat['date'] = last_message.added_at
        result.append(curr_chat)
    return JsonResponse({'result': result})
