import pandas as pd
import pickle

with open('models/initial_recomendation.pkl', 'rb') as f:
    initial_recomendation = pickle.load(f)
with open('data/product.pkl', 'rb') as f:
    product = pickle.load(f)


def getRecomendInitial():
    recommendation_list = []

    for pos, product_name in enumerate(initial_recomendation, start=1):
        product_info = product[product['product_name'] == product_name].iloc[0]
        product_id = int(product_info['product_id'])

        recommendation_list.append({
            'pos': pos,
            'product_id': product_id,
            'product_name': product_name
        })

    return recommendation_list
