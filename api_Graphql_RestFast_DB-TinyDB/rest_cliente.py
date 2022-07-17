from fastapi import FastAPI
from models.cliente.cliente_base_model import Cliente
from typing import List


app = FastAPI()

dbClientesMemory: List[Cliente] = []

@app.get('/clientes')
def getAllClientes():
  return dbClientesMemory


@app.post('/criar_cliente')
def criarCliente(cliente: Cliente):
  dbClientesMemory.append(cliente)
  return {'message': 'OK ! Criado com Sucesso!'}