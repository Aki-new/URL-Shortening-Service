# URL Shortening Service

[Español](README.es.md) | English

A robust, lightweight, and high-performance RESTful API that shortens long URLs into unique, manageable short codes and handles high-speed redirections. Built as part of the [roadmap.sh](https://roadmap.sh/projects/url-shortening-service) backend challenges series.

---

## 🚀 Features

- **URL Shortening**: Convert long web links into safe, alphanumeric short codes.
- **Custom Short Codes**: Allows optional user-defined custom aliases (with automatic length and character validation).
- **Fast Redirection**: Instantly route short codes (`/abc123`) back to their original destination via standard HTTP status codes (`302 Found`).
- **Access Analytics**: Tracks precise click/access counters for each generated short URL.
- **Input Validation**: Rigorous checks for input format, valid structural URLs, and string constraints to protect backend stability.
- **Data Persistence**: Clear segregation of the persistence mechanism using standard relational storage models or structured JSON schemas.

---

## 🛠️ System Architecture & Logic

The service implements a clean, layered design that completely decouples logic, API endpoints, and data layers:

1. **API Endpoints (Controller Layer)**: Validates incoming HTTP requests, checks payload structures, and maps correct HTTP response headers and status codes.
2. **Business Logic (Service Layer)**: Handles hash/code generation algorithms, checks uniqueness, increments statistical counters, and manages business constraints.
3. **Data Access (Persistence Layer)**: Abstracts read/write interactions with the datastore.

### Shortening & Hashing Logic
When a long URL is received:
- If a custom alias is provided, the system validates its pattern and checks its availability.
- If no code is provided, a randomized/hashed 6-character unique string is generated using an alphanumeric mapping dictionary (`[a-zA-Z0-9]`), preventing database collisions before insertion.

---

## 📋 API Specification

### 1. Shorten a URL
* **Endpoint:** `POST /shorten`
* **Content-Type:** `application/json`

**Request Body:**
```json
{
  "url": "https://example.com/",
  "shortCode": "example" 
}
```
**Note**: shortCode is optional; if it is not added, one is generated randomly
**Response** `(201 Created)`

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
### 2. Redirect a URL
* **Endpoint:** `GET /yourShortCode`
* **Content-Type:** `application/json`
* **Response:** `(302 Found)` (Redirects user directly to the target url).

### 3. Retrieve URL Statistics
* **Endpoint:** `GET /shorten/yourShortCode`
* **Response:** `(200 OK)`

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

### 4. Update an Existing Shortened URL
* **Endpoint:** PUT `/shorten/yourShortCode`
* **Content-Type:** application/json

**Request Body:**
```json
{
  "url": "https://www.linux.org/",
  "shortCode": "linux-web-site"
}
```
* **Note:** shortCode is opcional if you don't want to modify it
* **Response:** `(200 OK)`
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

### 5. Delete a Shortened URL
* Endpoint: `DELETE /shorten/yourShortCode`
* Response: `(204)` No Content

## 💻 How to Replicate and Run Locally
Follow these precise steps to set up, install dependencies, and host the environment on any external machine:

### Prerequisite Checklist
Ensure that your environment meets these requirements.

* Runtime: Python 3.10+
* Git installed on your operating system.

### 1. Clone Repository
``` bash
git clone https://github.com/Aki-new/URL-Shortening-Service
cd URL-Shortening-Service
```

### 2. Installation & Dependency Assembly
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python init_database.py
```

### 3. Launching the Server
Execute the application entry point:

Python execution: ``python main.py or uvicorn app.main:app --reload``

The local server will spin up instantly. Typically, you can access the server baseline at http://localhost:8080

## 🧪 Testing with cURL
You can test the functional compliance of your endpoints right from your terminal:

Create a shortened code:
```bash
curl -X POST http://localhost:8080/api/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "https://google.com"}'
```
Fetch specific analytics:
```bash
curl -X GET http://localhost:8080/shorten/YOUR_SHORT_CODE
```
