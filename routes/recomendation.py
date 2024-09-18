from fastapi import APIRouter
from config.db import conn
# from schemas.transaction import transactionsEntity

recomendation = APIRouter()

@recomendation.get('/getRecomendationByMemberId')
async def getRecomendationByMemberId(id):
  return None

@recomendation.get('/getRecomendationByProductId')
async def getRecomendationByProductId(id):
  return None
