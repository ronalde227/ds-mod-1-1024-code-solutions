import pickle
import pandas as pd
#trieving data frame using pickled object
#I could have all save the test data and retrieved it instead of saving the function
with open("load_data.pickle", "rb") as f:
    load_data = pickle.load(f)
df = load_data('application_test.csv')

with open("clean_data.pickle", "rb") as f:
    clean_data = pickle.load(f)

df = clean_data(df)

#encodign the data
with open("ce_target.pickle", "rb") as f:
    ce_target = pickle.load(f)

with open("encoder_features.pickle", "rb") as f:
    encode_features = pickle.load(f)

df[encode_features] = ce_target.transform(df[encode_features])


with open("binary_encoder.pickle", "rb") as f:
    binary_encoder = pickle.load(f)

df =  binary_encoder(df)

skid_id = df['SK_ID_CURR']
df = df.drop(['SK_ID_CURR'],axis=1)

#training data
with open("xgb_model.pickle", "rb") as f:
    xgb_model = pickle.load(f)

test_preds_proba = xgb_model.predict_proba(df)

submission_df = pd.DataFrame({'SK_ID_CURR': skid_id, 'TARGET': test_preds_proba[:,1]})

print(submission_df)

submission_df.to_csv('submission_class_pickle.csv', index=False)