from django.conf.urls import url

from . import views as mineral_views


urlpatterns = [
    url(r'(?P<pk>\d+)/$', mineral_views.mineral_detail, name='detail'),
    url(r'^$', mineral_views.index, name='index'),
]
