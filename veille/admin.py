from django.contrib import admin
from veille.models import Article, Source, Theme

# Register your models here.
admin.site.register(Article)
admin.site.register(Source)
admin.site.register(Theme)