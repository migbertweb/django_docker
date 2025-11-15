"""
Archivo: models.py

Descripción: Define el modelo Post para la aplicación de posts. El modelo incluye
             campos para título y contenido de los posts que se gestionan a través
             de la API REST.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Define la estructura de datos para los posts. Se utiliza en la API REST
     y en el panel de administración de Django.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
