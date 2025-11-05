from sqlalchemy.orm import Session
from .models import Registro
from .schemas import RegistroActualizado, RegistroBase, RegistroFuera, RegistroCreado

def get_all(db: Session):
    return db.query(Registro). all()

def get_by_id( id:int, db:Session):
    return db.query(Registro).filter(Registro.id == id).first()

def get_bad_records(db: Session):
    return db.query(Registro).filter(Registro.categoria == "bad").all()

def create_record(registro: dict, db: Session):
    try:
        if not registro:
            print("⚠️ No se recibió ningún registro válido.")
            return None
        
        mapeo = {
            "value": "valor_externo",
            "category": "categoria",
        }

        
        registro_mapeado = {
            mapeo.get(k, k): v for k, v in registro.items()
        }

        
        campos_modelo = Registro.__table__.columns.keys()
        registro_filtrado = {k: v for k, v in registro_mapeado.items() if k in campos_modelo}

        nuevo_registro = Registro(**registro_filtrado)
        db.add(nuevo_registro)
        db.commit()
        db.refresh(nuevo_registro)
        print(f" Registro guardado correctamente: {nuevo_registro}")
        return nuevo_registro

    except Exception as e:
        print(f" Error al guardar registro: {e}")
        db.rollback()

def update_record(id:int, registro: RegistroActualizado, db:Session):
    record_to_update = get_by_id(id=id, db=db)
    if record_to_update:
        for key, value in registro.dict().items():
            setattr(record_to_update, key, value)
        db.commit()
        db.refresh(record_to_update)
    return record_to_update

def delete_record(id: int, db: Session):
    remove_record = get_by_id(id=id, db=db)
    if remove_record:
        db.delete(remove_record)
        db.commit()
    return remove_record
