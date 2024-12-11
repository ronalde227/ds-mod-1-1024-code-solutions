# -*- coding: utf-8 -*-
"""training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ue6nBOvu22ABJchrJq3ONwWESAiJjLl4
"""

import pandas as pd
import pickle
from implementation_functions import *

df = load_data('application_train.csv')

with open("load_data.pickle", "wb") as f:
    pickle.dump(load_data,f)

df = clean_data(df)
with open("clean_data.pickle", "wb") as f:
    pickle.dump(clean_data,f)

df, category_list, ce_target = encode_data(df)
#saving target encoder
with open("ce_target.pickle", "wb") as f:
    pickle.dump(ce_target, f)

df = binary_encoder(df)

with open("binary_encoder.pickle", "wb") as f:
    pickle.dump(binary_encoder, f)

with open("encoder_features.pickle", "wb") as f:
    pickle.dump(category_list,f)



xtrain, xtest, ytrain, ytest = split_data(df)

print('Running train_model*********************************')
xgb_model, start_time, end_time = train_model(xtrain, ytrain)
with open("xgb_model.pickle", "wb") as f:
    pickle.dump(xgb_model,f)

