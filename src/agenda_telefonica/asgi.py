"""
Configuração ASGI para o projeto agenda_telefonica.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agenda_telefonica.settings')

application = get_asgi_application()
