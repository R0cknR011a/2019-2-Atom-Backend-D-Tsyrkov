from django.http import HttpResponseNotAllowed, JsonResponse
from members.forms import MemberForm
from members.models import Member
from rest_framework.decorators import api_view
import json


@api_view(['POST'])
def create(request):
    data = json.loads(request.body)
    form = MemberForm(data)
    if form.is_valid():
        member = form.save()
        return JsonResponse({
            'success': True,
            'chat ID': member.user.id
        })
    return JsonResponse({'errors': form.errors}, status=400)


@api_view(['GET'])
def get_all(request):
    result = Member.objects.all().values()
    return JsonResponse({'members': list(result)})

@api_view(['POST'])
def add_chat(request):
    username = json.loads(request.body)
    return JsonResponse({'username': username})
