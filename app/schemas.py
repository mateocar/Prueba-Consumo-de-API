from pydantic import BaseModel
from datetime import datetime

class RegistroBase(BaseModel):
    valor_externo: int
    categoria: str
    user_id: str

class RegistroCreado(RegistroBase):
    pass

class RegistroActualizado(RegistroBase):
    intentos: int

class RegistroFuera(RegistroBase):
    id: int
    intentos: int
    ultima_descarga: datetime

    class Config:
        orm_mode = True 

