from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def messages_list(request):
    if (request.method == 'GET'):
        return JsonResponse({'messages': 'here should be messages list'})
    return HttpResponseNotAllowed(['GET'])
