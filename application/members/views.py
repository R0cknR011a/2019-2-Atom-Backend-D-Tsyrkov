from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from members.forms import MemberForm
from members.models import Member

@csrf_exempt
def create(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        member = form.save()
        return JsonResponse({
            'success': True,
            'chat ID': member.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = Member.objects.all().values()
        return JsonResponse({'members': list(result)})
    return HttpResponseNotAllowed(['GET'])

