# 📤 Guía: Subir a GitHub

Sigue estos pasos para subir tu proyecto a GitHub:

## Paso 1: Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Completa los datos:
   - **Repository name**: `Arc_software`
   - **Description**: `Proyecto Django con sistema de productos y comentarios`
   - **Public**: Elige público o privado
   - **NO** marques "Initialize with README" (ya lo tenemos)
   - **NO** marques "Add .gitignore" (ya lo tenemos)

3. Click en **"Create repository"**

## Paso 2: Configurar Git Localmente

Abre terminal en la carpeta `djangocourse` y ejecuta:

```bash
cd /home/incognauta/Escritorio/Arc_Software/djangocourse
```

## Paso 3: Conectar repositorio local con GitHub

Reemplaza `TU_USUARIO` con tu usuario de GitHub:

```bash
git branch -M main
git remote add origin https://github.com/TU_USUARIO/Arc_software.git
git push -u origin main
```

**Nota**: Si usas **SSH** en lugar de HTTPS:
```bash
git remote add origin git@github.com:TU_USUARIO/Arc_software.git
git push -u origin main
```

## Paso 4: Ingresar credenciales

Si usas HTTPS, GitHub te pedirá:
- **Usuario**: Tu usuario de GitHub
- **Contraseña**: Usa un "Personal Access Token" (no tu contraseña)
  
### Crear Personal Access Token:
1. Ve a https://github.com/settings/tokens
2. Click en "Generate new token"
3. Dale permisos: `repo`, `workflow`
4. Copia el token y úsalo como contraseña

## Paso 5: ¡Listo!

Tu repositorio estará en:
```
https://github.com/TU_USUARIO/Arc_software
```

## Comandos útiles después

### Hacer push de cambios nuevos
```bash
git add .
git commit -m "Tu mensaje aquí"
git push
```

### Ver estado
```bash
git status
```

### Ver historial
```bash
git log --oneline
```

## Problemas comunes

### "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/Arc_software.git
```

### "Permission denied (publickey)"
Usa HTTPS en lugar de SSH, o configura tus keys SSH.

### "remote: Permission to user/repo.git denied"
Tu token no tiene los permisos correctos. Crea uno nuevo.

---

¿Necesitas ayuda? Avísame cuando termines y te verify que todo esté correcto.
