from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from . import views as mineral_views


urlpatterns = [
    url(r'(?P<pk>\d+)/$', mineral_views.mineral_detail, name='detail'),
    url(r'^$', mineral_views.index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
