from django.conf.urls import url
from .views import GetArticlesAPIView

urlpatterns = [
    url('getArticleList', GetArticlesAPIView.as_view(), name='article-list'),
]