"""
Archivo: views.py

Descripción: Vista para la subida de archivos (imágenes y multimedia). Maneja
             la recepción de archivos mediante POST, los guarda en el sistema
             de archivos y muestra la URL del archivo subido.

Autor: migbertweb

Fecha: 2025-11-15

Repositorio: https://github.com/migbertweb/django_docker

Licencia: MIT License

Uso: Procesa formularios de subida de archivos. Los archivos se guardan en
     mediafiles/ y se sirven a través de Nginx en producción o Django en desarrollo.

Nota: Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener 
derivados como código libre, especialmente para fines educativos.
"""
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")
