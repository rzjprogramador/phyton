from pydantic import BaseModel
from tinydb import TinyDB

exemplo01DB = TinyDB('Exemplo_01.json')

class Exemplo01(BaseModel):
  nome: str
  idade: int

request = { 'nome':'Rei', 'idade': 44 }

def InserirExemploNaTabela(model: Exemplo01):
  exemplo01DB.insert( model )

InserirExemploNaTabela(request)