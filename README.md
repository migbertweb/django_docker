# Django Docker Project

Aplicación Python-Django corriendo sobre Docker con configuración para desarrollo y producción.

## 📋 Descripción

Este proyecto es una aplicación Django que incluye:

- **API REST** para gestión de posts (título y contenido)
- **Sistema de subida de archivos** (imágenes y multimedia)
- **Configuración Docker** para desarrollo y producción
- **PostgreSQL** como base de datos
- **Nginx** como servidor web para producción
- **Gunicorn** como servidor WSGI para producción

## 🏗️ Arquitectura

El proyecto está estructurado en dos variantes:

### Desarrollo
- Django con servidor de desarrollo integrado
- Volúmenes montados para hot-reload
- Base de datos PostgreSQL en contenedor

### Producción
- Django con Gunicorn
- Nginx como reverse proxy y servidor de archivos estáticos/media
- Configuración optimizada para producción
- Volúmenes persistentes para archivos estáticos y media

## 📁 Estructura del Proyecto

```
django_docker/
├── app/                          # Aplicación Django principal
│   ├── hello_django/            # Configuración del proyecto Django
│   │   ├── settings.py          # Configuración de Django
│   │   ├── urls.py              # URLs principales
│   │   ├── wsgi.py              # Configuración WSGI
│   │   └── asgi.py              # Configuración ASGI
│   ├── post/                    # App de posts con API REST
│   │   ├── models.py            # Modelo Post
│   │   ├── api/                 # API REST
│   │   │   ├── views.py         # ViewSets de la API
│   │   │   ├── serializers.py   # Serializadores
│   │   │   └── router.py        # Router de la API
│   │   └── admin.py             # Configuración del admin
│   ├── upload/                  # App de subida de archivos
│   │   ├── views.py             # Vista de subida de archivos
│   │   ├── models.py            # Modelos (si los hay)
│   │   └── templates/           # Plantillas HTML
│   ├── manage.py                # Script de gestión de Django
│   ├── requirements.txt         # Dependencias Python
│   ├── Dockerfile               # Dockerfile para desarrollo
│   ├── Dockerfile.prod          # Dockerfile para producción
│   ├── entrypoint.sh            # Script de inicio (desarrollo)
│   └── entrypoint.prod.sh       # Script de inicio (producción)
├── nginx/                       # Configuración de Nginx
│   ├── Dockerfile               # Dockerfile de Nginx
│   └── nginx.conf               # Configuración de Nginx
├── docker-compose.yml           # Configuración Docker Compose (desarrollo)
├── docker-compose.prod.yml      # Configuración Docker Compose (producción)
└── LICENSE                      # Licencia MIT

```

## 🚀 Requisitos Previos

- Docker
- Docker Compose
- Git

## 📦 Instalación

### Desarrollo

1. Clona el repositorio:
```bash
git clone https://github.com/migbertweb/django_docker.git
cd django_docker
```

2. Crea un archivo `.env.dev` en la raíz del proyecto:
```env
DEBUG=1
SECRET_KEY=tu-secret-key-aqui
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```

3. Construye y ejecuta los contenedores:
```bash
docker-compose up --build
```

4. Realiza las migraciones:
```bash
docker-compose exec web python manage.py migrate
```

5. Crea un superusuario (opcional):
```bash
docker-compose exec web python manage.py createsuperuser
```

6. Accede a la aplicación:
   - Aplicación: http://localhost:8000
   - Admin: http://localhost:8000/admin

### Producción

1. Crea un archivo `.env.prod` en la raíz del proyecto:
```env
DEBUG=0
SECRET_KEY=tu-secret-key-seguro-aqui
DJANGO_ALLOWED_HOSTS=tu-dominio.com www.tu-dominio.com
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=hello_django
SQL_PASSWORD=password-seguro-aqui
SQL_HOST=db
SQL_PORT=5432
```

2. Crea un archivo `.env.prod.db`:
```env
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=password-seguro-aqui
POSTGRES_DB=hello_django_prod
```

3. Construye y ejecuta los contenedores:
```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

4. Realiza las migraciones:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```

5. Recopila archivos estáticos:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

6. Crea un superusuario:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

7. Accede a la aplicación:
   - Aplicación: http://localhost (puerto 80)

## 🔌 API REST

La API REST está disponible en `/api/` y proporciona endpoints para gestionar posts:

### Endpoints disponibles:

- `GET /api/post/` - Lista todos los posts
- `POST /api/post/` - Crea un nuevo post
- `GET /api/post/{id}/` - Obtiene un post específico
- `PUT /api/post/{id}/` - Actualiza un post completo
- `PATCH /api/post/{id}/` - Actualiza parcialmente un post
- `DELETE /api/post/{id}/` - Elimina un post

### Ejemplo de uso:

```bash
# Crear un post
curl -X POST http://localhost:8000/api/post/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Mi primer post", "content": "Contenido del post"}'

# Listar posts
curl http://localhost:8000/api/post/

# Obtener un post específico
curl http://localhost:8000/api/post/1/
```

## 📤 Subida de Archivos

La aplicación incluye una funcionalidad de subida de archivos accesible en la ruta raíz (`/`).

- Sube imágenes y archivos multimedia
- Los archivos se guardan en `mediafiles/`
- En producción, los archivos se sirven a través de Nginx

## 🛠️ Comandos Útiles

### Desarrollo

```bash
# Ver logs
docker-compose logs -f

# Ejecutar comandos Django
docker-compose exec web python manage.py <comando>

# Acceder al shell de Django
docker-compose exec web python manage.py shell

# Detener contenedores
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v
```

### Producción

```bash
# Ver logs
docker-compose -f docker-compose.prod.yml logs -f

# Ejecutar comandos Django
docker-compose -f docker-compose.prod.yml exec web python manage.py <comando>

# Detener contenedores
docker-compose -f docker-compose.prod.yml down

# Reiniciar servicios
docker-compose -f docker-compose.prod.yml restart
```

## 📚 Tecnologías Utilizadas

- **Django 4.1.1** - Framework web de Python
- **Django REST Framework** - Framework para APIs REST
- **PostgreSQL 14** - Base de datos relacional
- **Docker** - Contenedorización
- **Docker Compose** - Orquestación de contenedores
- **Nginx** - Servidor web y reverse proxy
- **Gunicorn** - Servidor WSGI para producción

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

**Nota especial:** Se recomienda encarecidamente, aunque no es obligatorio, que las obras derivadas mantengan este mismo espíritu de código libre y abierto, especialmente cuando se utilicen con fines educativos o de investigación.

## 👤 Autor

**Migbertweb**

- GitHub: [@migbertweb](https://github.com/migbertweb)
- Repositorio: [https://github.com/migbertweb/django_docker](https://github.com/migbertweb/django_docker)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Para preguntas o sugerencias, puedes abrir un issue en el repositorio.

---

**Nota:** Este proyecto usa Licencia MIT. Se recomienda (no obliga) mantener derivados como código libre, especialmente para fines educativos.
