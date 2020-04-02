from django.urls import path
from archive.views import *

urlpatterns = [
    path("", MainView.as_view(), name="MainArchiveView"),
]
