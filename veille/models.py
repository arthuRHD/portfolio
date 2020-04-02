import os
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()

    def __str__(self):
        return self.url

class Theme(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle
    

class Article(models.Model):
    title =  models.CharField(max_length=200)
    desc = models.TextField(default=None)
    body = RichTextUploadingField(null=True)
    thumbnail = models.ImageField(upload_to='upload/')
    date = models.DateField(auto_now_add=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    source = models.ManyToManyField(Source)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
