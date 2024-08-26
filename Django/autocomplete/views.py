from django.shortcuts import render
from .models import Autocomplete
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def autocompleteJSON(request):
    MAX_RESPONSE_PER_PAGE = 15
    qs = Autocomplete.objects.all().order_by('name')

    q: str = request.GET.get('q', '').strip()
    
    keywords = q.split()
    filt = Q()
    for keyword in keywords:
        filt &= Q(name__icontains=keyword) | Q(last__icontains=keyword)

    qs = qs.filter(filt)
    
    paginator = Paginator(qs,MAX_RESPONSE_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    json_data = []
    for item in page_obj:
        json_data.append({
            'id': item.id,
            'name': item.name,
            'last': item.last,
            'str': str(item)  # Utiliza str() para obtener la representación de texto del modelo
        })

    response_data = {
        'results': json_data,
        'page': page_obj.number,
        'total_pages': paginator.num_pages,
        'total_results': paginator.count
    }
    
    return JsonResponse(response_data, safe=False)

def example(request):
    return render(request,'autocomplete/index.html')