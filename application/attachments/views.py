from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from attachments.models import Attachment
from attachments.forms import AttachmentForm
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import login_required
import boto3


@login_required
@csrf_exempt
def get_all(request):
    if request.method == 'GET':
        result = Attachment.objects.all().values()
        return JsonResponse({'attachments': list(result)})
    return HttpResponseNotAllowed(['GET'])


@login_required
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


@login_required
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
    	form = AttachmentForm(request.POST, request.FILES)
    	if form.is_valid():
    		attach = form.save()
    		return JsonResponse({'success': attach.id})
    	return JsonResponse({'errors': form.errors}, status=400)
    return HttpResponseNotAllowed(['POST'])


@login_required
@csrf_exempt
def download_file(request):
	if request.method == 'GET':
		key = request.GET.get('key')
		session = boto3.session.Session()
		s3_client = session.client(
			service_name='s3',
			endpoint_url='http://hb.bizmrg.com',
			aws_access_key_id='6Da62vVLUi6AKbFnnRoeA3',
			aws_secret_access_key='gDYg4Bu15yUpNYGKmmpiVNGvLRWhUAJ3m1GGRvg8KTbU',
		)
		url = s3_client.generate_presigned_url('get_object',
			Params={
				'Bucket': 'tsyrkov_messanger_bucket',
				'Key': key,
				},
			ExpiresIn=300,
		)
		return JsonResponse({'success': url})
	return HttpMethodNotAllowed(['GET'])

