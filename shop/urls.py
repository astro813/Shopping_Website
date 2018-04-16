from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
     # /shop/
    url('^$', views.IndexView.as_view(), name='index'),
    # /shop/23/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]