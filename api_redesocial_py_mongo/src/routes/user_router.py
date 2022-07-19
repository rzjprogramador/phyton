from fastapi import APIRouter

user_router = APIRouter()

@user_router.get('/all', response_description = 'Rota para criar Usuario')
async def User():
  return {
    'status': 'Ok-1'
}