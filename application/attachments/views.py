from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from attachments.models import Attachment
from attachments.forms import AttachmentForm
from django.core.files.images import ImageFile
from attachments.forms import AttachmentChatCreateForm

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
    if request.method == 'POST':
        form = AttachmentChatCreateForm(request.POST)
        if form.is_valid():
            file_name = request.FILES.get('file')
            chat = request.POST.get('chat')
            result = Attachment.objects.filter(chat=chat)
            if result.count() < 1:
                return JsonResponse({'error': 'No match attachments found'})
            else:
                result.update(content=ImageFile(file_name))
                return JsonResponse({'success': file_name.name})
        return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])
