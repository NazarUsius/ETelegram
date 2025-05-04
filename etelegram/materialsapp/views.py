from django.http import JsonResponse, HttpResponseNotFound
from .models import Material
from django.views.decorators.csrf import csrf_exempt
import json

def material_list(request):
    materials = Material.objects.all().order_by('-uploaded_at')
    data = []
    for m in materials:
        data.append({
            'id': m.id,
            'title': m.title,
            'description': m.description,
            'type': m.material_type,
            'url': m.url,
            'file': m.file.url if m.file else '',
            'image': m.image.url if m.image else '',
            'uploaded_at': m.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def material_delete(request, pk):
    if request.method == 'DELETE':
        try:
            m = Material.objects.get(pk=pk)
            m.delete()
            return JsonResponse({'status': 'deleted'})
        except Material.DoesNotExist:
            return HttpResponseNotFound('Material not found')
