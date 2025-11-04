from sqlalchemy.orm import Session
from .models import Registro
from .schemas import RegistroActualizado, RegistroBase, RegistroFuera, RegistroCreado

def get_all(db: Session):
    return db.query(Registro). all()

def get_by_id( id:int, db:Session):
    return db.query(Registro).filter(Registro.id == id).first()

def get_bad_records(db: Session):
    return db.query(Registro).filter(Registro.categoria == "bad").all()

def create_record(registro: RegistroCreado, db: Session):
    new_record = Registro(**registro.model_dump())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def update_record(id:int, registro: RegistroActualizado, db:Session):
    record_to_update = get_by_id(id=id, db=db)
    if record_to_update:
        for key, value in registro.model_dump().items():
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
