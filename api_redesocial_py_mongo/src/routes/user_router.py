from fastapi import APIRouter, Body
from models.user import User

user_router = APIRouter()

@user_router.get('/inicio')
def Inicio():
  return { 'messagem': 'Inicio User' }

@user_router.post('/create', response_description = 'Rota para criar Usuario')
async def CreateUser(user: User = Body(...)):
  return {
    "message": "User criado com Sucesso"
}