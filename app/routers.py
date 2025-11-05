from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import crud, schemas, services


router = APIRouter(tags=["datos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/registros")
def registros_listados(db: Session = Depends(get_db)):
    return crud.get_all(db=db)

@router.post("/registros")
def create_registro(registro: schemas.RegistroCreado, db: Session = Depends(get_db)):
    db_registros = crud.RegistroCreado(registro, db)
    return db_registros

@router.put("/registros/{id}")
def update_registro(id: int, registro: schemas.RegistroActualizado, db: Session = Depends(get_db)):
    updated_registro = crud.update_record(id=id, registro=registro, db=db)
    return updated_registro


@router.delete("/registros/{id}")
def delete_registro(id: int, db : Session = Depends(get_db)):
    return crud.delete_record(id=id, db=db)


@router.post("/proceso/carga-inicial")
def proceso_carga_inicial(db: Session = Depends(get_db)):
    services.carga_inicial(db=db)
    return {"message": "Carga de datos iniciales completado"}

@router.post("/proceso/mejora")
def proceso_mejorad(db: Session = Depends(get_db)):
    services.mejorar_registros(db=db)
    return{"message": "Registros mejorados"}
