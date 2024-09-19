from fastapi import APIRouter
from controller.updateTransactionData import updateTransactionData
from controller.updateRecomender import updateRecomenderModel
from utils.response import success, error
update = APIRouter()

@update.get('/updateAll')
async def updateAll():
    try:
        updateTransactionData()
        updateRecomenderModel()
        return success("Transaction and recomender updating succesfully!")
    except Exception as e:
        return error("Transaction and recomender updating is not completed!", e)
        
@update.get('/updateTransaction')
async def updateTransaction():
    try:
        updateTransaction(  )
        return success("Transaction updating successfully!")
    except Exception as e:
        return error("Transaction updating is not completed!", e)

@update.get('/updateRecomender')
async def updateRecomender():
    try:
        updateRecomenderModel()
        return success("Recomender updating successfully!")
    except Exception as e:
        return error("Recomender updating is not completed!", e)