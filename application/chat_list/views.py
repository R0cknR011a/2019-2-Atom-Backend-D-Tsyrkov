from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

rick_example = ['Timon', 'Morty', 'Dock']
morty_example = [7, 8, 9] 
@csrf_exempt
def rick(request):
    if (request.method == 'GET'):
        return JsonResponse({'rick': rick_example})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def morty(request):
    if (request.method == 'GET'):
        return JsonResponse({'morty': morty_example})
    return HttpResponseNotAllowed(['GET'])
