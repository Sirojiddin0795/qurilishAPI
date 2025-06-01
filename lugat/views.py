from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Term, Category, SearchLog
from .serializers import TermSerializer, CategorySerializer
from django.db.models import Q
import json

@csrf_exempt
def term_list(request):
    if request.method == 'GET':
        sort = request.GET.get('sort', 'word')
        terms = Term.objects.all().order_by(sort)
        serializer = TermSerializer(terms, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def term_detail(request, pk):
    try:
        term = Term.objects.get(pk=pk)
    except Term.DoesNotExist:
        return JsonResponse({'error': 'So‘z topilmadi'}, status=404)

    if request.method == 'GET':
        serializer = TermSerializer(term)
        return JsonResponse(serializer.data)

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def term_search(request):
    query = request.GET.get('q', '')
    if query:
        terms = Term.objects.filter(Q(word__icontains=query) | Q(definition__icontains=query))
        found = terms.exists()
        SearchLog.objects.create(word=query, found=found)
        if found:
            serializer = TermSerializer(terms, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'So‘z topilmadi'}, status=404)
    return JsonResponse({'error': 'Qidiruv so‘zi yo‘q'}, status=400)

@csrf_exempt
def topic_terms(request, category_id):
    if request.method == 'GET':
        terms = Term.objects.filter(category_id=category_id)[:20]
        serializer = TermSerializer(terms, many=True)
        return JsonResponse(serializer.data, safe=False)
