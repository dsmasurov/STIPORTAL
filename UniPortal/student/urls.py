from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^NIRS/$', views.NIRSListView.as_view(), name='NIRS'),
    re_path(r'^NIRS/(?P<pk>\d+)$', views.NIRS_detail_view, name='NIRS-detail'),
    re_path(r'^article/$', views.ArticleListView.as_view(), name='article'),
    re_path(r'^comp/$', views.CompListView.as_view(), name='comp'),
]