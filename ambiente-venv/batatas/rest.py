from fastapi import FastAPI
from classExemplo2 import Exemplo02
# from exemplo_01 import Exemplo01, InserirExemploNaTabela

app = FastAPI()

@app.get('/home')
def home():
  return { 'message': 'Alo Home'}

@app.post('/criar-exemplo')
def criarExemplo(request: Exemplo02):
  print(request)
  return request
  # resposta = InserirExemploNaTabela(request)
  # return resposta