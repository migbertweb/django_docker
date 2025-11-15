"""
Archivo: views.py

Descripción: ViewSets de la API REST para el modelo Post. Proporciona endpoints
             CRUD completos (Create, Read, Update, Delete) para gestionar posts
             a través de la API REST.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Define el ViewSet que maneja todas las operaciones de la API REST de posts.
     Incluye listado, creación, lectura, actualización y eliminación de posts.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
