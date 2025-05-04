from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from .models import Material
from django.views.decorators.csrf import csrf_exempt
import json

def material_list(request):
    materials = Material.objects.all().order_by('-uploaded_at')
    return render(request, 'materials/list.html', {'media_list': materials})

@csrf_exempt
def material_delete(request, pk):
    m = get_object_or_404(Material, pk=pk)
    m.delete()
    return redirect('material_list')

