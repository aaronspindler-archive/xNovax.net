from django.http import JsonResponse

from .helpers import get_IP
from .models import Fingerprint, IP


def fingerprint_save(request):
    if request.method == 'POST':
        if request.POST['murmur']:
            ip_address = get_IP(request)

            ip = IP()
            ip.address = ip_address
            ip.save()
            fingerprint = Fingerprint(hash=request.POST['murmur'], ip=ip).save()

            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})
