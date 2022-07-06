from requests import get
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def root():
  return {
    'mensagem': 'Hello Fast Api >> 1 ---'
  }

@app.get('/postar/{nome}/{sobrenome}/{idade}')
async def postar(nome, sobrenome, idade):
  return {
    'nome': nome,
    'sobrenome': sobrenome,
    'idade': idade
}

@app.get('/saudacao/{mensagem}')
async def saudacao(mensagem: str):
  texto = f'Ola {mensagem}'
  return { 'saudacao': texto}

@app.get('/quadrado/{numero}')
async def quadrado(numero: int):
  result = numero * numero
  texto = f'O Quadrado de {numero} é {result}'
  return {'resultado': texto}