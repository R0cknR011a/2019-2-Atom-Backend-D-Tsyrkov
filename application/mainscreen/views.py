from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def mainscreen(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponseNotAllowed(['GET'])
