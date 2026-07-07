# Servicio de Acortamiento de URL

Español | [English](README.es.md)

Una API RESTful robusta, ligera y de alto rendimiento que acorta URL largas en códigos cortos únicos y fáciles de gestionar, y maneja redirecciones de alta velocidad. Desarrollada como parte de la serie de desafíos de backend de [roadmap.sh](https://roadmap.sh/projects/url-shortening-service).

---

## 🚀 Funcionalidades

- **Acortamiento de URL**: Convierte enlaces web largos en códigos cortos alfanuméricos seguros.

- **Códigos cortos personalizados**: Permite alias personalizados definidos por el usuario (con validación automática de longitud y caracteres).

- **Redireccionamiento rápido**: Enruta instantáneamente los códigos cortos (`/abc123`) a su destino original mediante códigos de estado HTTP estándar (`302 Found`).

- **Análisis de acceso**: Realiza un seguimiento preciso de los clics y accesos para cada URL corta generada.
- **Validación de entrada**: Comprobaciones rigurosas del formato de entrada, URL con estructura válida y restricciones de cadena para proteger la estabilidad del backend.

- **Persistencia de datos**: Clara segregación del mecanismo de persistencia mediante modelos de almacenamiento relacional estándar o esquemas JSON estructurados.

---

## 🛠️ Arquitectura y lógica del sistema

El servicio implementa un diseño limpio y por capas que desacopla completamente la lógica, los endpoints de la API y las capas de datos:

1. **Endpoints de la API (Capa de controlador)**: Valida las solicitudes HTTP entrantes, comprueba la estructura de la carga útil y asigna los encabezados de respuesta HTTP y los códigos de estado correctos.

2. **Lógica de negocio (Capa de servicio)**: Gestiona los algoritmos de generación de hash/código, comprueba la unicidad, incrementa los contadores estadísticos y administra las restricciones de negocio.

3. **Acceso a datos (Capa de persistencia)**: Abstrae las interacciones de lectura/escritura con el almacén de datos.

### Lógica de acortamiento y hash
Cuando se recibe una URL larga:
- Si se proporciona un alias personalizado, el sistema valida su patrón y comprueba su disponibilidad.

- Si no se proporciona ningún código, se genera una cadena única de 6 caracteres aleatoria/hash mediante un diccionario de mapeo alfanumérico (`[a-zA-Z0-9]`), lo que evita colisiones con la base de datos antes de la inserción.

--

## 📋 Especificación de la API

### 1. Acortar una URL
* **Endpoint:** `POST /shorten`
* **Content-Type:** `application/json`

**Body Request:**
```json
{
  "url": "https://example.com/",
  "shortCode": "example"
}
```
**Nota**: shortCode es opcional; Si no se agrega, se genera uno aleatoriamente.
**Respuesta:** `(201 Creado)`

```json
{
  "id": 1,
  "url": "https://example.com/",
  "shortCode": "example",
  "createdAt": "2026-07-06T13:25:00Z",
  "updatedAt": "2026-07-06T13:25:00Z",
  "accessCount": 0
}
```
### 2. Redirigir una URL
* **Endpoint:** `GET /yourShortCode`
* **Content-Type:** `application/json`
* **Respuesta:** `(302 Encontrado)` (Redirige al usuario directamente a la URL de destino).

### 3. Recuperar estadísticas de URL
* **Endpoint:** `GET /shorten/yourShortCode`
* **Respuesta:** `(200 OK)`

```json
{
  "id": 1,
  "url": "https://example.com/",
  "shortCode": "yourShortCode",
  "createdAt": "2026-07-06T13:25:00Z",
  "updatedAt": "2026-07-06T13:25:00Z",
  "accessCount": 42
}
```

### 4. Actualizar una URL acortada existente
* **Endpoint:** PUT `/shorten/yourShortCode`
* **Content-Type:** application/json

**Body Request:**
```json
{
  "url": "https://www.linux.org/",
  "shortCode": "linux-web-site"
}
```
* **Nota:** shortCode es opcional si no desea modificarlo
* **Respuesta:** `(200 OK)`
```json
{
  "id": 1,
  "url": "https://www.linux.org/",
  "shortCode": "linux-web-site",
  "createdAt": "2026-07-06T13:25:00Z",
  "updatedAt": "2026-07-06T13:30:00Z",
  "accessCount": 22
}
```

### 5. Eliminar una URL acortada
* Endpoint: `DELETE /shorten/yourShortCode`
* Respuesta: `(204)` Sin contenido

## 💻 Cómo replicar y ejecutar Localmente
Siga estos pasos para configurar, instalar dependencias y alojar el entorno en cualquier máquina externa:

### Lista de requisitos previos
Asegúrese de que su entorno cumpla con estos requisitos.

* Entorno de ejecución: Python 3.10 o superior
* Git instalado en su sistema operativo.

### 1. Clonar el repositorio
``` bash
git clone https://github.com/Aki-new/URL-Shortening-Service
cd URL-Shortening-Service
```

### 2. Instalación y configuración de dependencias
```bash
python -m venv venv
source venv/bin/activate # En Windows, usar: venv\Scripts\activate
pip install -r requirements.txt
python init_database.py
```

### 3. Iniciar el servidor
Ejecutar el punto de entrada de la aplicación:

Ejecución de Python: ``python main.py o uvicorn app.main:app --reload``

El servidor local se iniciará al instante. Normalmente, puedes acceder a la configuración base del servidor en http://localhost:8080

## 🧪 Pruebas con cURL
Puedes comprobar la funcionalidad de tus endpoints directamente desde la terminal:

Crea un código shortCode:
```bash
curl -X POST http://localhost:8080/api/shorten \
-H "Content-Type: application/json" \
-d '{"url": "https://google.com"}'
```
Obtén datos analíticos específicos:
```bash
curl -X GET http://localhost:8080/shorten/YOUR-SHORT-CODE
```