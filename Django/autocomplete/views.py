from django.shortcuts import render
from .models import Autocomplete
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
# Create your views here.

def autocompleteJSON(request):
    MAX_RESPONSE = 15
    qs = Autocomplete.objects.all().order_by('name')

    q = request.GET.get('q', '')
    
    keywords = q.split()
    filt = Q()
    for keyword in keywords:
        filt &= Q(name__icontains=keyword) | Q(last__icontains=keyword)

    qs = qs.filter(filt)[:MAX_RESPONSE]

    json_data = []
    for item in qs:
        json_data.append({
            'id': item.id,
            'name': item.name,
            'last': item.last,
            'str': str(item)  # Utiliza str() para obtener la representación de texto del modelo
        })

    return JsonResponse(json_data, safe=False)

def example(request):
    return render(request,'autocomplete/index.html')