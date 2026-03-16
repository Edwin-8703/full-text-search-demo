from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Document

def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        search_vector = SearchVector('title', 'content', 'doc_type')
        search_query = SearchQuery(query)
        results = Document.objects.annotate(
            rank=SearchRank(search_vector, search_query)
        ).filter(rank__gte=0.001).order_by('-rank')

    return render(request, 'documents/search.html', {
        'query': query,
        'results': results,
    })