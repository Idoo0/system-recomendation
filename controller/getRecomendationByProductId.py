from fastai.collab import CollabDataLoaders, collab_learner
from fastai.tabular.all import *
import pickle

with open('models/byProduct/product_factors.pkl', 'rb') as f:
    product_factors = pickle.load(f)
with open('data/dls.pkl', 'rb') as f:
    dls = pickle.load(f)
with open('data/product.pkl', 'rb') as f:
    product = pickle.load(f)


def getRecomendByProduct(product_id):

    product_info = product[product['product_id'] == int(product_id)]
    product_name = None
    if not product_info.empty:
        product_name = product_info.iloc[0]['product_name']
        print("produk tersedia!")
    else:
        print("produk tidak tersedia!")
        return None

    idx = dls.classes['product_name'].o2i[product_name]
    distances = nn.CosineSimilarity(dim=1)(
        product_factors, product_factors[idx][None])
    idx = distances.argsort(descending=True)[1:11]

    recommendations = dls.classes['product_name'][idx]
    recommendation_list = []

    for pos, product_name in enumerate(recommendations, start=1):
        product_info = product[product['product_name'] == product_name].iloc[0]
        product_id = int(product_info['product_id'])

        recommendation_list.append({
            'pos': pos,
            'product_id': product_id,
            'product_name': product_name
        })

    return recommendation_list
