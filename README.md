# Prueba-Consumo-de-API

## 🚀 1. Instalación y configuración

### 🔧 Requisitos previos
- Python 3.9 o superior  
- pip  
- Virtualenv (opcional)

### 📦 Instalación
```bash
# Clona el repositorio
git clone https://github.com/mateocar/Prueba-Consumo-de-API.git
cd PRUEBA-CONSUMO-DE-API

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación FastAPI
uvicorn app.main:app --reload

La API estará disponible en:
👉 http://127.0.0.1:8000/docs

# Arquitectura del proyecto
PRUEBA-CONSUMO-DE-API/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routers.py
│   ├── schemas.py
│   ├── services.py
│
├── prueba.db
├── requirements.txt
└── README.md

3. Esquema de la tabla

La base de datos prueba.db contiene la tabla registros con la siguiente estructura:

__tablename__ = "registros"

id = Column(Integer, primary_key=True, index=True)
valor_externo = Column(Integer, nullable=False)
categoria = Column(String, nullable=False)
user_id = Column(String, nullable=False)
intentos = Column(Integer, default=1)
ultima_descarga = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

4. Consultas SQL principales
Total de llamadas iniciales
SELECT COUNT(*) AS llamadas_iniciales FROM registros;

Total de barridos (mejoras)
SELECT SUM(intentos) AS total_barridos
FROM registros;

Total de llamadas (iniciales + mejoras)
SELECT COUNT(*) AS total_registros,
       SUM(intentos) AS total_llamadas
FROM registros;

Distribución por categoría
SELECT categoria, COUNT(*) AS total_por_categoria
FROM registros
GROUP BY categoria
ORDER BY total_por_categoria DESC;
