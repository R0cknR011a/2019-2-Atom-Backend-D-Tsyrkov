from django.http import JsonResponse
from users.models import User
from members.models import Member
from users.forms import UserForm
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def search_username(request):
    username = request.GET.get('username')
    result = User.objects.filter(username__contains=username).values()
    return JsonResponse({'users': list(result)})

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
    username = User.objects.get(username=request.GET['username'])
    users = [element['username'] for element in User.objects.exclude(username=username).values()]
    chats = [element['chat_id'] for element in Member.objects.filter(user=username).values()]
    members = [element['user_id'] for element in Member.objects.filter(chat__in=chats).exclude(user=username).values()]
    not_allowed_users = [element['username'] for element in User.objects.filter(id__in=members).values()]
    result = [element for element in users if element not in not_allowed_users]
    return JsonResponse({'users': result})
