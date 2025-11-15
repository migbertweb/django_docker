"""
Archivo: wsgi.py

Descripción: Configuración WSGI (Web Server Gateway Interface) para el proyecto.
             Expone la aplicación Django como un callable WSGI para servidores
             como Gunicorn en producción.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Punto de entrada WSGI para servidores de producción como Gunicorn.
     Se utiliza en el despliegue de producción con Docker.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
"""
WSGI config for hello_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

application = get_wsgi_application()
