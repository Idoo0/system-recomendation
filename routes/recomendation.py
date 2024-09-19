from fastapi import APIRouter
from controller.getRecomendationByMemberId import getRecomendByMember
from controller.getRecomendationByProductId import getRecomendByProduct
from controller.getRecomendationInitial import getRecomendInitial
from utils.response import success, error
recomendation = APIRouter()

@recomendation.get('/getRecomendationByMemberId')
async def getRecomendationByMemberId(id):
    result = getRecomendByMember(id)
    if result:
        return success("Product recommendations successfully retrieved!", result)
    else:
        return error("Unable to retrieve product recommendations!")

@recomendation.get('/getRecomendationByProductId')
async def getRecomendationByProductId(id):
    result = getRecomendByProduct(id)
    if result:
        return success("Product recommendations successfully retrieved!", result)
    else:
        return error("Unable to retrieve product recommendations!")

@recomendation.get('/testgetRecomendationInitial')
async def getRecomendationInitial():
    result = getRecomendInitial()
    if result:
        return success("Product recommendations successfully retrieved!", result)
    else:
        return error("Unable to retrieve product recommendations!")
