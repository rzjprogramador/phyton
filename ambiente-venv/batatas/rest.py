from fastapi import FastAPI
from exemplo_classes.classe_exemplo_02 import Exemplo03
from exemplo_02.exemplo_01 import Exemplo01, InserirExemploNaTabela

app = FastAPI()

@app.get('/home')
def home():
  return { 'message': 'Alo Home'}

@app.post('/criar-exemplo')
def criarExemplo(request: Exemplo01):
  print(request)
  # return request
  resposta = InserirExemploNaTabela(request)
  return resposta