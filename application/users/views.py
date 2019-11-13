from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from users.forms import UserForm

@csrf_exempt
def search_username(request):
    if (request.method == 'GET'):
        username = request.GET.get('username')
        result = User.objects.filter(username__contains=username).values()
        return JsonResponse({'users': list(result)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def create(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        return JsonResponse({
            'success': True,
            'chat ID': user.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = User.objects.all().values('id', 'username', 'bio')
        return JsonResponse({'users': list(result)})
    return HttpResponseNotAllowed(['GET'])

