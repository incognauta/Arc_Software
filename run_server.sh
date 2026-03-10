#!/bin/bash

# Script para ejecutar Django limpiando caché automáticamente

cd /home/incognauta/Escritorio/Arc_Software/djangocourse/helloworld

echo "🧹 Limpiando caché..."

# Limpiar __pycache__
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null

# Limpiar archivos .pyc y .pyo
find . -type f -name "*.pyc" -delete 2>/dev/null
find . -type f -name "*.pyo" -delete 2>/dev/null

# Matar procesos Django anteriores en puerto 8000
echo "🛑 Cerrando procesos anteriores..."
lsof -ti :8000 2>/dev/null | xargs kill -9 2>/dev/null

sleep 1

echo "✅ Caché limpiado. Iniciando servidor..."
echo ""

# Activar venv y ejecutar runserver
source ../django_course_env/bin/activate
python manage.py runserver
