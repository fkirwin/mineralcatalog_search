"""
WSGI config for mineralcatalog_search project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application
from django.db import utils

from minerals.models import Mineral

try:
    Mineral.ingest_data_from_json_file()
except (utils.DatabaseError, utils.DataError) as e:
    print(e)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mineralcatalog_search.settings')

application = get_wsgi_application()
