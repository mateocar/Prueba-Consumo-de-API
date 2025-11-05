import requests
from .crud import create_record, get_bad_records
from .config import API_BASE_URL, USER_ID

def obtener_datos_api():
    url = f"{API_BASE_URL}?user_id={USER_ID}"
    print(f"🔗 Consultando API en: {url}")
    try:
        response = requests.get(url)
        print(f" Código de respuesta: {response.status_code}")

        # Mostrar el contenido crudo de la respuesta
        print(f"Contenido bruto: {response.text[:500]}")  # solo los primeros 500 caracteres

        if response.status_code == 200:
            api_response = response.json()
            return api_response.get("data", api_response)
        else:
            print("Error al consumir API externa.")
            return None
    except Exception as e:
        print(f"Error en la solicitud: {e}")
        return None

def carga_inicial(db, limit=100):
    for i in range(limit):
        data = obtener_datos_api()
        if not data:
            continue
        try:
            create_record(registro=data, db=db)
            print(" Registro creado correctamente.")
        except Exception as e:
            print(f" Error al guardar registro: {e}")

def mejorar_registros(db):
    registro_malo = get_bad_records(db)
    for registro in registro_malo:
         data = obtener_datos_api()
         if data["category"] in ["medium", "good"]:
             registro.valor_externo = data["value"]
             registro.categoria = data["category"]
             registro.intentos += 1
             db.commit()
