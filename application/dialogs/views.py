from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dialogs.forms import MessageForm
from dialogs.models import Message

@csrf_exempt
def create(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save()
        return JsonResponse({
            'success': True,
            'message ID': message.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = Message.objects.all().values()
        return JsonResponse({'messages': list(result)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def messages_with(request):
    if (request.method == 'GET'):
        chat = request.GET.get('chat_id')
        result = Message.objects.filter(chat=chat).values()
        return JsonResponse({'result': list(result)})
    return HttpResponseNotAllowed(['GET'])
