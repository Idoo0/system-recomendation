import pickle

with open('models/byMember/user_matrix.pkl', 'rb') as f:
    user_item_matrix = pickle.load(f)
with open('models/byMember/user_similarity.pkl', 'rb') as f:
    user_similarity_df = pickle.load(f)
with open('data/product.pkl', 'rb') as f:
    product = pickle.load(f)


def getRecomendByMember(user_id):
    user_id = int(user_id)
    num_recommendations = 10
    
    if user_id not in user_similarity_df.index:
        return None
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]

    similar_users_items = user_item_matrix.loc[similar_users].sum().sort_values(ascending=False)

    user_purchases = user_item_matrix.loc[user_id]
    recommendations = similar_users_items[user_purchases == 0].head(
        num_recommendations)

    recommendation_list = []

    for pos, product_name in enumerate(recommendations.index.tolist(), start=1):
        product_info = product[product['product_name'] == product_name].iloc[0]
        product_id = int(product_info['product_id'])

        recommendation_list.append({
            'pos': pos,
            'product_id': product_id,
            'product_name': product_name
        })

    return recommendation_list
