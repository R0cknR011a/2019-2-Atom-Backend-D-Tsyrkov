from django.shortcuts import render
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chats.models import Chat
from chats.forms import ChatForm


@csrf_exempt
def create_chat(request):
    form = ChatForm(request.POST)
    if form.is_valid():
        chat = form.save()
        return JsonResponse({
            'success': True,
            'chat ID': chat.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = Chat.objects.all().values()
        return JsonResponse({'chats': list(result)})
    return HttpResponseNotAllowed(['GET'])

