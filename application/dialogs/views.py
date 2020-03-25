from django.http import JsonResponse
from dialogs.forms import MessageForm, ReadMessageForm
from dialogs.models import Message
from members.models import Member
from chats.models import Chat
from users.models import User
from attachments.models import Attachment
from rest_framework.decorators import api_view
import boto3
import json
import requests

API_KEY = '2954bfc0-ded7-4d0f-a931-285e3bc63159'

@api_view(['POST'])
def create(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        session = boto3.session.Session()
        s3_client = session.client(
            service_name='s3',
            endpoint_url='http://hb.bizmrg.com',
            aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
            aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
        )
        user = User.objects.get(username=request.POST['username'])
        chats = Member.objects.filter(user=user)
        for chat in chats:
            op = Member.objects.filter(chat=chat.chat).exclude(user=user).get()
            if op.user.username == request.POST['opponent']:
                result = chat.chat
                break
        message = Message(content=request.POST['content'], chat=result, user=user, added_at=request.POST['date'])
        message.save()
        response = [message.id]
        result.last_message = '(' + request.POST['attach_type'] + ') ' +\
            request.POST['content'] if request.POST['attach_type'] != 'none' else request.POST['content']
        result.save()
        chat.last_read_message = Message.objects.filter(chat=result).filter(user=op.user).last()
        chat.save()
        attachs = {}
        attachs['type'] = request.POST['attach_type']
        if request.POST['attach_type'] == 'geolocation':
            attachment = Attachment(
                chat=result,
                user=user,
                message=message,
                attach_type='geolocation',
                url=request.POST['content'],
            )
            attachment.save()
            attachs['url'] = attachment.url
            response.append(attachment.id)
        else:
            attachs['url'] = []

        for file in request.FILES:
            key = 'attachments/' + request.POST['attach_type'] + result.topic + '/' + str(hash(file))
            s3_client.put_object(
                Bucket='tsyrkov_messanger_bucket',
                Key=key,
                Body=request.FILES[file],
            )
            attachment = Attachment(
                chat=result,
                user=user,
                message=message,
                attach_type=request.POST['attach_type'],
                url=key,
            )
            attachment.save()
            attachs['url'].append(s3_client.generate_presigned_url('get_object', Params={
                'Bucket': 'tsyrkov_messanger_bucket',
                'Key': attachment.url,
            }, ExpiresIn=3600))
            response.append(attachment.id)

        # send message to client
        if attachs['type'] == 'audio':
            attachs['url'] = attachs['url'][0]
        avatar = s3_client.generate_presigned_url('get_object', Params={
            'Bucket': 'tsyrkov_messanger_bucket',
            'Key': message.user.avatar,
        }, ExpiresIn=3600)
        command_1 = {
            'method': 'publish',
            'params': {
                'channel': op.user.username + '_with_' + user.username,
                'data': {
                    'avatar': avatar,
                    'opponent': message.user.username,
                    'topic': result.topic,
                    'author': message.user.username,
                    'last_message': result.last_message,
                    'read': False,
                    'date': 'T'.join(message.added_at.split(' ')),
                    'message': message.content,
                    'attachments': attachs,
                }
            }
        }
        command_2 = {
            'method': 'publish',
            'params': {
                'channel': op.user.username,
                'data': {
                    'avatar': avatar,
                    'opponent': message.user.username,
                    'topic': result.topic,
                    'author': message.user.username,
                    'last_message': result.last_message,
                    'read': False,
                    'date': 'T'.join(message.added_at.split(' ')),
                    'message': message.content,
                    'attachments': attachs,
                }
            }
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'apikey ' + API_KEY,
        }
        requests.post(url='http://localhost:9000/api', data=json.dumps(command_1), headers=headers)
        requests.post(url='http://localhost:9000/api', data=json.dumps(command_2), headers=headers)
        return JsonResponse({'success': response})
    return JsonResponse({'errors': form.errors}, status=400)


@api_view(['GET'])
def get_all(request):
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
        aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
    )
    username = User.objects.get(username=request.GET['username'])
    opponent = User.objects.get(username=request.GET['opponent'])
    chats = Member.objects.filter(user=username)
    for chat in chats:
        op = Member.objects.filter(chat=chat.chat).exclude(user=username).get()
        if op.user.username == request.GET['opponent']:
            curr_chat = chat.chat
            break
    messages = Message.objects.filter(chat=curr_chat)
    me = Member.objects.filter(chat=curr_chat).filter(user=username).get()
    op_last_message = Message.objects.filter(chat=curr_chat).filter(user=op.user).last()
    me.last_read_message = op_last_message
    me.save()
    op_last_read_message = op.last_read_message
    result = []
    for message in messages:
        avatar = s3_client.generate_presigned_url('get_object', Params={
                    'Bucket': 'tsyrkov_messanger_bucket',
                    'Key': message.user.avatar,
                }, ExpiresIn=3600)
        data = {
            'author': message.user.username,
            'message': message.content,
            'date': message.added_at,
            'avatar': avatar,
            'attachments': {}
        }
        if message.user == username:
            if op_last_read_message is None:
                data['read'] = False
            else:
                if message.id > op_last_read_message.id:
                    data['read'] = False
                else:
                    data['read'] = True
        if message.user == opponent:
            data['read'] = True
        attachments = Attachment.objects.filter(chat=curr_chat).filter(message=message)
        if len(attachments) > 0:
            if attachments[0].attach_type == 'geolocation':
                data['attachments']['type'] = 'geolocation'
                data['attachments']['url'] = attachments[0].url
            elif attachments[0].attach_type == 'audio':
                data['attachments']['type'] = 'audio'
                data['attachments']['url'] = s3_client.generate_presigned_url('get_object', Params={
                    'Bucket': 'tsyrkov_messanger_bucket',
                    'Key': attachments[0].url,
                }, ExpiresIn=3600)
            else:
                arr = []
                for attach in attachments:
                    arr.append(s3_client.generate_presigned_url('get_object', Params={
                        'Bucket': 'tsyrkov_messanger_bucket',
                        'Key': attach.url,
                    }, ExpiresIn=3600))
                data['attachments']['type'] = 'images'
                data['attachments']['url'] = arr

        # send notification to client
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'apikey ' + API_KEY,
        }
        command = {
            'method': 'publish',
            'params': {
                'channel': op.user.username + '_notify',
                'data': {
                    'opponent': username.username,
                }
            }
        }
        requests.post(url='http://localhost:9000/api', data=json.dumps(command), headers=headers)
        result.append(data)
    return JsonResponse({'messages': result})


@api_view(['POST'])
def read_message(request):
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        user = User.objects.get(username=request.POST['username'])
        chats = Member.objects.filter(user=user)
        for chat in chats:
            op = Member.objects.filter(chat=chat.chat).exclude(user=user).get()
            if op.user.username == request.POST['opponent']:
                curr_chat = chat.chat
                break
        message = Message.objects.filter(chat=curr_chat).last()
        member = Member.objects.filter(user=user).filter(chat=curr_chat).get()
        member.last_read_message = message
        member.save()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'apikey ' + API_KEY,
        }
        command_1 = {
            'method': 'publish',
            'params': {
                'channel': op.user.username + '_notify',
                'data': {
                    'opponent': user.username,
                }
            }
        }
        command_2 = {
            'method': 'publish',
            'params': {
                'channel': user.username + '_notify',
                'data': {
                    'opponent': op.user.username,
                }
            }
        }
        requests.post(url='http://localhost:9000/api', data=json.dumps(command_1), headers=headers)
        requests.post(url='http://localhost:9000/api', data=json.dumps(command_2), headers=headers)
        return JsonResponse({'message': member.last_read_message.content})
    return JsonResponse({'errors': form.errors}, status=400)
