"""
Archivo: urls.py

Descripción: Configuración de URLs principales del proyecto. Define las rutas
             de la aplicación incluyendo el admin de Django, la API REST de posts
             y la vista de subida de archivos.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Mapea las URLs a sus respectivas vistas. Incluye rutas para:
     - / (subida de archivos)
     - /admin/ (panel de administración)
     - /api/ (API REST de posts)

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
from post.api.router import router_posts

urlpatterns = [
    path("", image_upload, name="upload"),
    path('admin/', admin.site.urls),
    path('api/', include(router_posts.urls))

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
