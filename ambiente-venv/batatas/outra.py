from pydantic import BaseModel
from tinydb import TinyDB

outraDB = TinyDB('Outra.json')

class Outra(BaseModel):
  nome: str
  idade: int

# CLASSE BASEMODEL NAO PRECISO INSTANCIAR - 
# 1- CRIO UM DICIONARIO COM AS INFO DA INSTACIA 

request = { 'nome':'Rei', 'idade': 44 }

# 2 - FAZ FUNCAO QUE RECEBERA EMPACOTADO A CLASSE MODEL
# USA A TABELA. INSERT() ESPERANDO RECEBER UM MODEL EMPACOTADO QUE SERA O OBJ DA CLASSE BaseModel

def InserirOutra(model: Outra):
  outraDB.insert( outra )

# 3- EXECUTA A FUNCAO QUE INSERE OS DADOS REQUEST VINDO EM DICIONARIO/JSON 
def main():
  InserirOutra(request)
  
main()