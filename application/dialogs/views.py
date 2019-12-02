from django.http import JsonResponse
from dialogs.forms import MessageForm
from dialogs.models import Message
from members.models import Member
from chats.models import Chat
from users.models import User
from attachments.models import Attachment
from rest_framework.decorators import api_view
import boto3

@api_view(['POST'])
def create(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        user = User.objects.get(username=request.POST['username'])
        chats = Member.objects.filter(user=user)
        for chat in chats:
            op = Member.objects.filter(chat=chat.chat).exclude(user=user).get().user.username
            if op == request.POST['opponent']:
                result = chat.chat
                break
        message = Message(content=request.POST['content'], chat=result, user=user, added_at=request.POST['date'])
        message.save()
        response = [message.id]
        result.last_message = request.POST['content']
        result.save()
        if request.POST['attach_type'] == 'geolocation':
            attachment = Attachment(
                chat=result,
                user=user,
                message=message,
                attach_type='geolocation',
                url=request.POST['content'],
            )
            attachment.save()
            response.append(attachment.id)
        if len(request.FILES) > 0:
            session = boto3.session.Session()
            s3_client = session.client(
                service_name='s3',
                endpoint_url='http://hb.bizmrg.com',
                aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
                aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
		    )
            for file in request.FILES:
                key = 'attachments/' + request.POST['attach_type'] + 's/' + result.topic + '/' + str(hash(file))
                s3_client.put_object(
                    Bucket = 'tsyrkov_messanger_bucket',
                    Key = key,
                    Body = request.FILES[file],
                )
                attachment = Attachment(
                    chat=result,
                    user=user,
                    message=message,
                    attach_type=request.POST['attach_type'],
                    url=key,
                )
                attachment.save()
                response.append(attachment.id)
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
    chats = Member.objects.filter(user=username)
    for chat in chats:
        op = Member.objects.filter(chat=chat.chat).exclude(user=username).get().user.username
        if op == request.GET['opponent']:
            curr_chat = chat.chat
            break
    messages = Message.objects.filter(chat=curr_chat)
    result = []
    for message in messages:
        data = {
            'author': message.user.username,
            'message': message.content,
            'time': message.added_at,
            'attachments': {}
        }
        attachments = Attachment.objects.filter(chat=curr_chat).filter(message=message)
        if len(attachments) > 0:
            if len(attachments) == 1:
                if attachments[0].attach_type == 'geolocation':
                    data['attachments']['type'] = 'geolocation'
                    data['attachments']['url'] = attachments[0].url
                else:
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
        result.append(data)
    return JsonResponse({'messages': result})


@api_view(['GET'])
def messages_with(request):
    chat = request.GET.get('chat_id')
    result = Message.objects.filter(chat=chat).values()
    return JsonResponse({'result': list(result)})


@api_view(['POST'])
def read_message(request):
    message = request.GET.get('message_id')
    result = Message.objects.filter(id=message).values()
    return JsonResponse({
        'message': list(result)
    })
