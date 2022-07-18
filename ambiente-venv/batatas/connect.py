from tinydb import TinyDB
from model import Pessoa

pessoaDB = TinyDB('Pessoas.json')

def InserirPessoa(pessoa: Pessoa):
  pessoaDB.insert(
    {
      'nome': pessoa.nome,
      'idade': pessoa.idade,
      'CPF': pessoa.CPF
    }
  )