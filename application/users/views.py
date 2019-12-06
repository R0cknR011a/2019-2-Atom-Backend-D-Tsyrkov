from django.http import JsonResponse
from users.models import User
from members.models import Member
from users.forms import UserForm, UserAvatarForm
from rest_framework.decorators import api_view
import boto3

@api_view(['GET'])
def search_username(request):
    username = request.GET['username']
    result = [elem.username for elem in User.objects.exclude(username=username)]
    return JsonResponse({'users': result})

@api_view(['POST'])
def create(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({
            'success': True,
            'chat ID': user.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@api_view(['GET'])
def get_all(request):
    user = User.objects.get(username=request.GET['username'])
    other_users = [elem.username for elem in User.objects.exclude(username=user)]
    all_chats = []
    chats = Member.objects.filter(user=user)
    for chat in chats:
        all_chats.append(chat.chat)
    exist_chats = [Member.objects.filter(chat=elem).exclude(user=user).get().user.username for elem in all_chats]
    result = [elem for elem in other_users if elem not in exist_chats]
    print(other_users, exist_chats)
    return JsonResponse({'users': result})


@api_view(['GET'])
def get_settings(request):
    user = User.objects.get(username=request.GET['username'])
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
        aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
    )
    avatar = s3_client.generate_presigned_url('get_object', Params={
                    'Bucket': 'tsyrkov_messanger_bucket',
                    'Key': user.avatar,
                }, ExpiresIn=3600)
    result = {
        'avatar': avatar,
        'fullname': user.first_name + user.last_name,
        'bio': user.bio,
    }
    return JsonResponse({'result': result})

@api_view(['POST'])
def set_settings(request):
    form = UserForm(request.POST)
    if form.is_valid:
        user = User.objects.get(username=request.POST['username'])
        user.bio = request.POST['bio']
        user.first_name = request.POST['fullname'].split(' ')[0]
        user.last_name = request.POST['fullname'].split(' ')[1]
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'errors': form.errors})


@api_view(['POST'])
def set_avatar(request):
    form = UserAvatarForm(request.POST)
    if form.is_valid:
        session = boto3.session.Session()
        s3_client = session.client(
        service_name='s3',
        endpoint_url='http://hb.bizmrg.com',
        aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
        aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
        )
        s3_client.put_object(
                    Bucket = 'tsyrkov_messanger_bucket',
                    Key = 'avatars/' + request.POST['username'],
                    Body = request.FILES['avatar'],
        )
        user = User.objects.get(username=request.POST['username'])
        user.avatar = 'avatars/' + request.POST['username']
        user.save()
        return JsonResponse({'success': True})
    return JsonResponse({'errors': form.errors})
