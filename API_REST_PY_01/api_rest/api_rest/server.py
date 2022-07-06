from requests import get
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/hello')
async def root():
  return {
    'mensagem': 'Hello Fast Api >> 1 ---'
  }

# PARAMETRO DE CAMINHO PATH URL
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

# PARAMETRO DE ROTA
@app.get('/dobro')
async def dobro(numero: int, parametro2: str):
  res = numero * numero
  texto = parametro2.upper()
  return {
    'resultado': f'O dobro de {numero} é {res} e o segundo parametro enviado é {texto}'
}

# CAMPOS DEFINIDOS COM VALOR DEFAULT VIRAM OPCIONAIS APRA O UTILIZADOR

@app.get('/requisicao')
async def requisicao(nome: str, idade: int, opcional: str = 'meu id é 1'):
  return {
    'nome': nome,
    'idade': idade,
    'opcional': opcional
  }

  # ENVIADO NA URL: http://localhost:8000/requisicao?nome=Reinado&idade=44
  # RESPOSTA JSON: {"nome":"Reinado","idade":44,"opcional":"meu id é 1"}

  # REQUISICOES POST : VIA CORPO DA REQUISICAO
  #  METODO POST :: RECEBENDO OBJ DO TIPO CLASSEMODEL COM AS INFORMACOES DO UTILIZADOR E RESPONDENDO O OBJ RECEBIDO. 
class Produto(BaseModel):
  nome: str
  valor: float

@app.post('/produtos')
async def produtos(produto: Produto):
  print(produto)
  return produto