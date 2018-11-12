from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
import debug_toolbar

from . import views as mineral_views


urlpatterns = [
    url(r'(?P<pk>\d+)/$', mineral_views.mineral_detail, name='detail'),
    url(r'search/$', mineral_views.search_by_name, name='search'),
    url(r'^$', mineral_views.index, name='index'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
