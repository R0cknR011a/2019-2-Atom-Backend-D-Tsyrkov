from django.shortcuts import render
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chats.models import Chat

@csrf_exempt
def create_chat(request, is_group_chat, topic, last_message):
    if (request.method == 'POST'):
        if is_group_chat == 1:
            is_group_chat = True
        elif is_group_chat == 0:
            is_group_chat = False
        else:
            return JsonResponse({'error': 'invalid is_group_chat input (0, 1)'})
        chat = Chat(is_group_chat=is_group_chat, topic=topic, last_message=last_message)
        chat.save()
        return JsonResponse({'chats': 'succeed'})
    return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = Chat.objects.all().values()
        return JsonResponse({'chats': list(result)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def alena_chat(request):
    if (request.method == 'GET'):
        return JsonResponse({'chats': 'here should be chat with Alena'})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def anton_chat(request):
    if (request.method == 'GET'):
        return JsonResponse({'chats': 'here should be chat with Anton'})
    return HttpResponseNotAllowed(['GET'])
