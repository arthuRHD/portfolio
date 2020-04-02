from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from veille.models import Article, Theme, Source
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

class CiThemeView(TemplateView):
    template_name = 'veille/ci.html'
class EthThemeView(TemplateView):
    template_name = 'veille/eth.html'
class LegiThemeView(TemplateView):
    template_name = 'veille/legi.html'
        
class ArticleList(View):
    def get(self, request):
        return render(request, 'veille/veille.html', {'articles_list': Article.objects.all() })

class ArticleDetails(View):
    def get(self, request, article_id):
        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404("Il n'a pas d'articles")
        return render(request, 'veille/details.html', {'article': article})
