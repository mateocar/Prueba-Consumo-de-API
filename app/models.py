from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Registro(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True, index=True)
    valor_externo = Column(Integer, nullable=False)
    categoria = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    intentos = Column(Integer, default=1)
    ultima_descarga = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())