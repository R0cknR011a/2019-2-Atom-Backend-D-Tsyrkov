from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from attachments.models import Attachment
from attachments.forms import AttachmentForm

@csrf_exempt
def get_all(request):
    if (request.method == 'GET'):
        result = Attachment.objects.all().values()
        return JsonResponse({'attachments': list(result)})
    return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def create(request):
    form = AttachmentForm(request.POST)
    if form.is_valid():
        attachment = form.save()
        return JsonResponse({
            'success': True,
            'attachment ID': attachment.id
        })
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def upload_file(request):
    print(request.FILES.get('file'))
    return JsonResponse({'success': True})
