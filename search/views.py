from django.shortcuts import render 
from django.db.models import Q
from veille.models import Article
# Create your views here.

def search(request):
    q = request.GET.get('q')
    if q:
        articles_search = Article.objects.filter(
            Q(title__icontains=q) | Q(desc__icontains=q) | Q(body__icontains=q) | Q(date__icontains=q)
        )
    else:
        articles_search = ""
    return render(request, "search/search.html", {'articles_search': articles_search})