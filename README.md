## Tarea: Configurar Django con MySQL y acceder al admin

1. **Configurar la base de datos MySQL en `settings.py`:**

- Abre el archivo `settings.py` de tu proyecto Django.
- Busca la sección `DATABASES` y reemplázala con la siguiente configuración para MySQL:
  ```python
  DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'nombre_de_tu_base_de_datos',
       'USER': 'tu_usuario',
       'PASSWORD': 'tu_contraseña',
       'HOST': 'localhost',  # O la dirección del servidor MySQL
       'PORT': '3306',       # Puerto predeterminado de MySQL
    }
  }
  ```
- Asegúrate de instalar el conector de MySQL.

2. **Crear un superusuario:**

- Ejecuta el siguiente comando para crear un superusuario:
  ```bash
  docker-compose run web python manage.py createsuperuser
  ```

3. **Acceder al panel de administración de Django:**

- Inicia el servidor de desarrollo:
  ```bash
  docker-compose up
  ```
- Abre tu navegador y ve a `http://localhost:8000/admin`.
- Inicia sesión con las credenciales del superusuario que creaste.

> **Nota:** Asegúrate de que tu base de datos MySQL esté en funcionamiento y accesible desde tu contenedor Docker antes de realizar estas configuraciones.

> **Pista:** Hay que hacer cambios en el requirements.txt para instalar la libreria de mysql de python y hacer un build (buscar información).

## Comandos útiles para Docker y Django

### Listar contenedores

```bash
docker ps
```

### Acceder al bash de un contenedor específico

```bash
docker exec -it <container_id> bash
```

> Reemplaza `<container_id>` con el ID o nombre del contenedor al que deseas acceder.

### Hacer migraciones

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

### Crear un superusuario

```bash
docker-compose run web python manage.py createsuperuser
```

## Comandos iniciales que hemos usado

### Crea el proyecto de Django

```bash
docker-compose run web python django-admin startproject prueba
```

### Hace un build

```bash
docker-compose build
```

### Inicia los contenedores

```bash
docker-compose up
```
