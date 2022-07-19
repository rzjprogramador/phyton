from fastapi import APIRouter

user_router = APIRouter()

@user_router.get('/user', response_description = 'Rota criar User', tags=['User'])
async def User():
  return {
    'status': 'Ok-1'
}