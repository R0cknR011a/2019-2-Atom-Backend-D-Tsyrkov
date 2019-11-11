from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def members_list(request):
    if (request.method == 'GET'):
        return JsonResponse({'members': 'here should be members list'})
    return HttpResponseNotAllowed(['GET'])
