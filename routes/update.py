from fastapi import APIRouter
from config.db import conn
from controller.updateTransactionData import updateTransactionData
# from schemas.transaction import transactionsEntity

update = APIRouter()

@update.get('/updateTransaction')
async def updateTransaction():
    result = updateTransactionData()
    return result

@update.get('/updateRecomender')
async def updateRecomender():
  return None
