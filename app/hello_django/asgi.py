"""
Archivo: asgi.py

Descripción: Configuración ASGI (Asynchronous Server Gateway Interface) para el
             proyecto. Expone la aplicación Django como un callable ASGI para
             servidores asíncronos y WebSockets.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Punto de entrada ASGI para servidores asíncronos. Preparado para futuras
     implementaciones de WebSockets o funcionalidades asíncronas.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
"""
ASGI config for hello_django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

application = get_asgi_application()
