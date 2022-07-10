from typing import Optional
from fastapi import FastAPI
from sqlmodel import (
  SQLModel, Field, create_engine
)

engine = create_engine('sqlite:///database.db') # CRIA A ENGINE
SQLModel.metadata.create_all(engine) # CRIA O BANCO DE DADOS

app = FastAPI()

class Cliente(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  nome: str
  idade: int

@app.get('/')
def home():
  return {'message': 'DEU BOM'}