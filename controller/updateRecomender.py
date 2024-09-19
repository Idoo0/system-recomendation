import pickle
import pandas as pd
from config.db import conn
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from fastai.collab import CollabDataLoaders, collab_learner
from fastai.tabular.all import *

load_dotenv()

db = conn["product_recommendation"]
collection = db["crm"]


def updateRecomenderModel():

    transactions = list(collection.find())
    df_transactions = pd.DataFrame(transactions)

    product_ids_to_remove = [3596, 7667, 14729, 9414, 4259, 14730, 3654, 4420, 8711, 4426,
                             4161, 14671, 4422, 4423, 2453, 4261, 4155, 4260, 14976, 14955, 14975, 15008, 14966, 15972]
    df_transactions = df_transactions[~df_transactions['product_id'].isin(
        product_ids_to_remove)]

    product = df_transactions[['product_id', 'product_name']]
    with open('data/product.pkl', 'wb') as f:
        pickle.dump(product, f)

    df_transactions = df_transactions[['member_id', 'product_name']]

    grouped_data = df_transactions.groupby(
        ['member_id', 'product_name']).size().reset_index(name='quantity')

    # FOR INITIAL RECOMENDATION
    grouped_data_product = df_transactions.groupby(
        'product_name').size().reset_index(name='quantity')
    sorted_grouped_data_product = grouped_data_product.sort_values(
        'quantity', ascending=False)
    initial_rec = sorted_grouped_data_product['product_name'].head(10).tolist()

    with open('models/initial_recomendation.pkl', 'wb') as f:
        pickle.dump(initial_rec, f)

    # FOR REC BY MEM ID
    data = grouped_data
    user_item_matrix = data.pivot_table(
        index='member_id', columns='product_name', values='quantity', fill_value=0)

    user_similarity = cosine_similarity(user_item_matrix)

    user_similarity_df = pd.DataFrame(
        user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

    with open('models/byMember/user_matrix.pkl', 'wb') as f:
        pickle.dump(user_item_matrix, f)

    with open('models/byMember/user_similarity.pkl', 'wb') as f:
        pickle.dump(user_similarity_df, f)

    # FOR REC BY PROD ID
    data = grouped_data

    data['quantity'] = (data['quantity'] - data['quantity'].min()) / \
        (data['quantity'].max() - data['quantity'].min())

    dls = CollabDataLoaders.from_df(
        data, user_name='member_id', item_name='product_name', rating_name='quantity', bs=64)

    learn = collab_learner(dls, n_factors=100, y_range=(0.5, 5.5), wd=1e-2)

    lr_min = learn.lr_find()

    learn.fit_one_cycle(15, lr_min)

    product_factors = learn.model.i_weight.weight

    with open('models/byProduct/product_factors.pkl', 'wb') as f:
        pickle.dump(product_factors, f)

    with open('data/dls.pkl', 'wb') as f:
        pickle.dump(dls, f)
