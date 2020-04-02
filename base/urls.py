from django.urls import path
from base.views import *

urlpatterns = [
    path("", Index.as_view(), name="Index"),
    #path("", index, name="Index"),
    path("portfolio/",PortfolioView.as_view(), name="PortfolioView"),
    path("contact/", ContactView.as_view(), name="ContactView"),
    path("copyright/", CopyrightView.as_view(), name="CopyrightView"),
]
