# Instrucciones de Ejecución - API Fardo

## 🚀 Inicio Rápido

### 1. Activar el entorno virtual
```bash
source venv/bin/activate
```

### 2. Instalar dependencias (solo primera vez)
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la API
```bash
uvicorn main:app --reload --port 8000
```

### 4. Acceder a la documentación
- API Docs (Swagger): http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

## 📋 Endpoints Disponibles

### Información de Empresa
- `GET /company` - Información completa de Fardo
- `GET /team` - Equipo de Fardo
- `GET /value-propositions` - Diferenciadores y propuestas de valor
- `GET /comparison` - Comparación con alternativas

### Servicios y Planes
- `GET /services` - Lista de servicios
- `GET /services/{service_id}` - Servicio específico
- `GET /plans` - Planes de suscripción
- `GET /plans/{plan_id}` - Plan específico
- `GET /methodology` - Metodología de 4 fases

### Educación
- `GET /faq` - Preguntas frecuentes
- `GET /faq/{faq_id}` - FAQ específica
- `GET /glossary` - Glosario de términos (AEO, GEO, LLMO, etc.)
- `GET /glossary/{term}` - Definición de término específico
- `GET /resources` - Recursos educativos (guías, webinars, etc.)

### Plataforma y Tecnología
- `GET /ai-engines` - Motores de IA cubiertos (ChatGPT, Gemini, Perplexity, Claude)
- `GET /ai-engines/{engine_id}` - Motor de IA específico
- `GET /roadmap` - Roadmap del producto
- `GET /updates` - Actualizaciones recientes

### Métricas
- `GET /industry-benchmarks` - Benchmarks por industria

### Utilidades
- `GET /search?q={query}` - Búsqueda general
- `GET /health` - Health check

## 🧪 Probar la API

```bash
# Ejecutar script de pruebas
python test_api.py
```

## 📦 Deployment

### Railway/Render
El proyecto incluye un `Procfile` listo para deployment en Railway o Render.

### Variables de entorno
No se requieren variables de entorno para esta versión.

## 🌐 Versión actual
**v1.3.0** - Incluye todos los nuevos endpoints de FAQs, Glosario, AI Engines, Value Propositions, Benchmarks, Resources, Comparison y Updates.

