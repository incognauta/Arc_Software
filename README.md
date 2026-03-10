# Arc_Software - Django Course

Proyecto Django con sistema de productos, comentarios y administración de usuarios.

## 📋 Características

- ✅ Listado de productos
- ✅ Vista individual de producto con detalles
- ✅ Sistema de comentarios
- ✅ Formulario de creación de productos
- ✅ Base de datos SQLite
- ✅ Admin de Django
- ✅ Bootstrap 5 para diseño responsive

## 🚀 Inicio Rápido

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/Arc_software.git
cd Arc_software/djangocourse
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv django_course_env
source django_course_env/bin/activate  # En Linux/Mac
# o en Windows:
django_course_env\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones
```bash
cd helloworld
python manage.py migrate
```

### 5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
bash ../run_server.sh
```

O manualmente:
```bash
python manage.py runserver
```

El servidor estará disponible en `http://127.0.0.1:8000`

## 📁 Estructura Proyecto

```
djangocourse/
├── helloworld/              # Proyecto Django principal
│   ├── pages/              # Aplicación de páginas y productos
│   │   ├── models.py       # Modelos (Product, Comment)
│   │   ├── views.py        # Vistas
│   │   ├── urls.py         # Rutas URL
│   │   ├── templates/      # Templates HTML
│   │   └── management/     # Comandos personalizados
│   ├── helloworld_project/ # Configuración del proyecto
│   ├── manage.py           # Script de gestión Django
│   └── db.sqlite3          # Base de datos
├── run_server.sh           # Script para ejecutar servidor limpiando caché
├── CACHE_GUIDE.md          # Guía para evitar problemas de caché
└── COMANDOS_DJANGO.txt     # Comandos útiles de Django
```

## 🛠️ Comandos Útiles

### Limpiar caché
```bash
python manage.py clearcache
```

### Crear nuevas migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Crear superusuario
```bash
python manage.py createsuperuser
```

### Acceder a admin
```
http://127.0.0.1:8000/admin
```

### Seed datos de prueba
```bash
python manage.py seed_products
```

## 📝 Modelos

### Product
- `name` (CharField): Nombre del producto
- `price` (IntegerField): Precio
- `description` (TextField): Descripción
- `image` (ImageField): Imagen del producto
- `created_at` (DateTimeField): Fecha de creación
- `updated_at` (DateTimeField): Fecha actualización

### Comment
- `product` (ForeignKey): Referencia al producto
- `description` (TextField): Texto del comentario

## 🔧 Tecnologías

- Django 6.0.2
- Python 3.12
- SQLite3
- Bootstrap 5.3.0
- Pillow (para imágenes)

## 📄 Licencia

Este proyecto es de aprendizaje y uso educativo.

## 👨‍💻 Autor

Desarrollado durante un curso de Django.
