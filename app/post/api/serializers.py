"""
Archivo: serializers.py

Descripción: Serializador de Django REST Framework para el modelo Post. Convierte
             instancias del modelo Post a formato JSON y viceversa para la API REST.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Serializa y deserializa los datos del modelo Post (id, title, content) para
     su uso en la API REST.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from rest_framework.serializers import ModelSerializer
from post.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
