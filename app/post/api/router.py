"""
Archivo: router.py

Descripción: Configuración del router de Django REST Framework para la API de posts.
             Registra las rutas de la API REST y genera automáticamente los endpoints
             CRUD para el modelo Post.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Define el router que genera las URLs de la API REST. Se incluye en las
     URLs principales del proyecto en hello_django/urls.py bajo el prefijo /api/.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=PostApiViewSet)
