from fastapi import FastAPI
from .database import Base, engine
from .routers import router

Base.metadata.create_all(bin=engine)
 
app = FastAPI(title=" Prueba")

app.include_router(router)