from django.core.management.base import BaseCommand
import os
import shutil
import subprocess

class Command(BaseCommand):
    help = 'Limpiar caché de Python y __pycache__'

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        
        self.stdout.write(self.style.WARNING('🧹 Limpiando caché...'))
        
        # Eliminando __pycache__
        for root, dirs, files in os.walk(base_dir):
            if '__pycache__' in dirs:
                pycache_dir = os.path.join(root, '__pycache__')
                try:
                    shutil.rmtree(pycache_dir)
                    self.stdout.write(f"  ✓ Eliminado: {pycache_dir}")
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"  ✗ Error: {e}"))
        
        # Eliminando archivos .pyc
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith('.pyc') or file.endswith('.pyo'):
                    try:
                        os.remove(os.path.join(root, file))
                        self.stdout.write(f"  ✓ Eliminado: {file}")
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"  ✗ Error: {e}"))
        
        self.stdout.write(self.style.SUCCESS('✅ Caché limpiado correctamente!'))
