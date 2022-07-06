from requests import get
from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def root():
  return {
    'mensagem': 'Hello Fast Api >> 1 ---'
  }