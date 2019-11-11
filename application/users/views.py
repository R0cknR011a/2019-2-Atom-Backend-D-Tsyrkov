from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User

@csrf_exempt
def search_username(request, username):
    if (request.method == 'GET'):
        result = User.objects.filter(username__contains=username).values()
        return JsonResponse({'users': list(result)})
    return HttpResponseNotAllowed(['GET'])


