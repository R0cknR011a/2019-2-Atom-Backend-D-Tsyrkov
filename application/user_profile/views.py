from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

timon_example = [1, 2, 3]
pumba_example = [4, 5, 6] 
@csrf_exempt
def timon(request):
    if (request.method == 'GET'):
        return JsonResponse({'chats': timon_example})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def pumba(request):
    if (request.method == 'GET'):
        return JsonResponse({'chats': pumba_example})
    return HttpResponseNotAllowed(['GET'])
