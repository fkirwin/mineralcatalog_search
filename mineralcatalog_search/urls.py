"""mineralcatalog_search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

from minerals import views as mineral_views

urlpatterns = [
    url(r'^minerals/', include(('minerals.urls', 'minerals'),  namespace='minerals')),
    url(r'search/$', mineral_views.search_by_name, name='search'),
    url('admin/', admin.site.urls),
    url(r'^$', mineral_views.index, name='index'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
