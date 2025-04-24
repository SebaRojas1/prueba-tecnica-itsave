# Prueba técnica de ItSave

## Descripción
Pequeña aplicación FullStack de una lista de tareas (To-Do) que permite agregar, eliminar y marcar tareas como completadas.

Tecnologias principales utilizadas:
- Frontend: Vue y Tailwind
- Backend: Django
- Base de datos: MySQL

## Requisitos previos
Para su ejecución es necesario tener instalado lo siguiente:
- Node.js
- npm
- Python
- pip
- MySQL

## Instalación
Debes tener una terminal abierta para lo siguiente:
### 1. Clonar el repositorio
```bash
git clone https://github.com/SebaRojas1/prueba-tecnica-itsave.git
```

### 2. Configurar el Backend
#### Crear un entorno virtual
```bash
cd prueba-tecnica-itsave
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS o Linux:
source venv/bin/activate

cd backend
# Instalar dependencias
pip install -r requirements.txt
```

#### Configurar la base de datos
1. Crear la base de datos MySQL
```bash
# Inicio de sesión, tambien puedes hacerlo con una interfaz grafica
mysql -u root -p
```

```sql
CREATE DATABASE tasks_list_app CHARACTER SET UTF8MB4 COLLATE utf8mb4_general_ci;
CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON tasks_list_app.* TO 'user_name'@'localhost';
FLUSH PRIVILEGES;
```
2. Crea un archivo .env dentro de la carpeta de __backend__ y usa la siguiente configuración:
```dotenv
# DB configuration
DB_NAME=tasks_list_app
DB_USER=root # Se recomienda usar el root, pero puedes usar el otro con privilegios similares
DB_PASSWORD=<contraseña>
DB_HOST=localhost
DB_PORT=3306 # El puerto por defecto de MySQL es 3306

# Frontend configuration
FRONTEND_URL=http://localhost:4000
```

#### Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Iniciar el servidor Backend
```bash
python manage.py runserver
```

El Backend estará disponible para recibir peticiones en http://localhost:8000

### 3. Configurar el Frontend
1. Crea un archivo .env dentro de la carpeta de __frontend__ y usa la siguiente configuración:
```dotenv
VITE_BACKEND_URL = http://localhost:8000
```
2. Instala las dependencias e inicia el servidor Frontend
En una terminal distinta debes hacer lo siguiente:

```bash
cd frontend
# Instala todas las dependencias que requiere el Frontend
npm install
# Inicia el servidor en modo desarrollo
npm run dev
```

El Frontend estará funcionando en el puerto http://localhost:4000/, que es donde se debe ingresar para utilizar la aplicación.