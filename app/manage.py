#!/usr/bin/env python
"""
Archivo: manage.py

Descripción: Script de gestión de Django. Permite ejecutar comandos administrativos
             como migraciones, creación de superusuarios, servidor de desarrollo, etc.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Punto de entrada principal para comandos de gestión de Django.
     Ejemplo: python manage.py runserver, python manage.py migrate

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
