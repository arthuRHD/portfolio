from django.conf.urls import url, include
from django.urls import path
from veille.views import *
from django.conf import settings

urlpatterns = [    
    path("", ArticleList.as_view(), name="ArticleList"),
    path("<int:article_id>/", ArticleDetails.as_view(), name="ArticleDetails"),    
    path("ci/", CiThemeView.as_view(), name="CiThemeView"),
    path("eth/", EthThemeView.as_view(), name="EthThemeView"),
    path("legi", LegiThemeView.as_view(), name="LegiThemeView"),
]