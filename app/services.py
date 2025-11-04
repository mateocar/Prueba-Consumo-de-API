import requests
from .crud import create_record, get_bad_records
from .config import API_BASE_URL, USER_ID

def obtener_datos_api():
    response = requests.get(f"{API_BASE_URL}?user_id={USER_ID}")
    data = response.json()
    return data

def carga_inicial(db, limit=100):
    for i in range(limit):
        data = obtener_datos_api()
        create_record(registro=data, db=db)

def mejorar_registros(db):
    registro_malo = get_bad_records(db)
    for registro in registro_malo:
         data = obtener_datos_api()
         if data["category"] in ["medium", "good"]:
             registro.valor_externo = data["value"]
             registro.categoria = data["category"]
             registro.intentos += 1
             db.commit()
