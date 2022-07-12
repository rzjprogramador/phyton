from typing import Optional
from fastapi import FastAPI
from sqlmodel import (
  SQLModel, Field, create_engine, select, Session
)

engine = create_engine('sqlite:///database.db') # CRIA A ENGINE

app = FastAPI()

class Cliente(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  nome: str
  idade: int

SQLModel.metadata.create_all(engine) # CRIA O BANCO DE DADOS ## OBS: TEM QUE FICAR APOS A CLASSE PRA TER A VISAO E CRIAR NO BANCO

@app.get('/')
def home():
  return {'message': 'DEU BOM'}

@app.get('/cliente')
def get_cliente():
  query = select(Cliente)
  with Session(engine) as session:
    result = session.execute(query).scalars().all()
    return result