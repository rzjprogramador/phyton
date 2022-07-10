from tinydb import TinyDB
from model.cliente import Cliente

DB = TinyDB("Clientes.json")

def inserir(model: Cliente):
  DB.insert({
    "CPF": model.CPF,
    "nome": model.nome,
    "nascimento": model.nascimento
  })

def mostrarTodos():
  todos = DB.all()
  return todos

def deletarCliente(cliente):
  pass