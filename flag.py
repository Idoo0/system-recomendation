import os
from controller.updateRecomender import updateRecomenderModel

flag_file = [
  'data/dls.pkl',
  'data/product.pkl',
  'models/initial_recomendation.pkl',
  'models/byMember/user_matrix.pkl',
  'models/byMember/user_similarity.pkl',
  'models/byProduct/product_factors.pkl'
]

all_files_exist = all(os.path.exists(file) for file in flag_file)

if not all_files_exist:
    updateRecomenderModel()