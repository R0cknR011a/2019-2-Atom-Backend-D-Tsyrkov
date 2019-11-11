from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def attachments_list(request):
    if (request.method == 'GET'):
        return JsonResponse({'attachments': 'here should be attachments list'})
    return HttpResponseNotAllowed(['GET'])
