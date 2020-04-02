from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from base.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from veille.models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class Index(ListView):
    model = Article
    context_object_name = 'articles'
    template_name='base/index.html'
    paginate_by = 6
    queryset = Article.objects.all()

class PortfolioView(TemplateView):
    template_name = 'base/portfolio.html'

class CopyrightView(TemplateView):
    template_name = 'base/copyright.html'

class ContactView(View):
    template = "base/contact.html"
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['arthur.richard2299@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.', status=403)
            return HttpResponseRedirect("/veille/")

    def get(self, request):
        form = ContactForm()
        return render(request, self.template, {'form': form})      
