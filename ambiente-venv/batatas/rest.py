from fastapi import FastAPI
from exemplo_01 import Exemplo01, InserirExemploNaTabela

app = FastAPI()

@app.get('/home')
def home():
  return { 'message': 'Alo Home'}

@app.post('/criar-exemplo')
def criarExemplo(request: Exemplo01):
  resposta = InserirExemploNaTabela(request)
  return resposta