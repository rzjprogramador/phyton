from tinydb import TinyDB, Query
from model.cliente import Cliente

DB = TinyDB("Clientes.json")
cliente = Query()

def inserir(model: Cliente):
  DB.insert({
    "CPF": model.CPF,
    "nome": model.nome,
    "nascimento": model.nascimento
  })

def mostrarTodos():
  todos = DB.all()
  return todos

def deletarCliente(cpf: int):
  if DB.search(cliente.CPF == cpf):
    DB.remove(cliente.CPF == cpf)
    print(f'OK! Deletado com Sucesso!')
  else:
    print('OPS! Cliente nao encontrado!')

def atualizarCliente(cpf: int, model: Cliente):
  if DB.search(cliente.CPF == cpf):
    DB.remove(cliente.CPF == cpf)
    inserir(model)

  else:
    print('OPS! Cpf nao existente!')
