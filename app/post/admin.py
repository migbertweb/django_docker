"""
Archivo: admin.py

Descripción: Configuración del panel de administración de Django para el modelo Post.
             Permite gestionar los posts desde el panel de administración con
             visualización personalizada de los campos.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Registra el modelo Post en el admin de Django con configuración personalizada
     para mostrar id y título en la lista.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.contrib import admin
from post.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
