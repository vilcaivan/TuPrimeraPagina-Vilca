# TuPrimeraPagina+Vilca
Pre-Entrega n°3 - Coderhouse - Comision: 78325

#Estructura general
TuPrimeraPagina+Vilca/
├── README.md
├── manage.py
├── webdjango/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── blog/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        ├── base.html
        ├── form.html

# Cómo usar el proyecto

1. Dscargar este repositorio.
2. Instalar las dependencias: pip install django
3. Crear las migraciones y migrar la base de datos: python manage.py makemigrations python manage.py migrate
4. Crear un superuser para acceder al admin (opcional): python manage.py createsuperuser
5. Ejecutar el servidor: python manage.py runserver
6. Desde el navegador, acceder a:
- `http://127.0.0.1:8000/` para la página principal.
- `http://127.0.0.1:8000/admin/` para gestionar datos con credenciales del superuser.
- Las rutas de formularios para agregar escritores, categorías, posts, y navegar entre rutas.

# Funciones

- Añadir escritores, categorías, y postear (con formularios, con escritor+categoria definido previamente)
- Herencia de plantillas con `base.html`.

