# -*- coding: utf-8 -*-
"""recommendation_systems_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hhWAmJqBnae-aBCrj4N__81LX4MZ-gNe
"""

import pandas as pd
import numpy as np
import matplotlib as plt

print("Creating models: Can take 30 sec - 2 minutes... ")
print("")
col_names = ['user_id', 'stream_id', 'streamer_username', 'time_start', 'time_stop']

df = pd.read_csv('100k_a.csv', names=col_names)

df.count()

#grouping by streamer
stream_count = df.groupby('streamer_username')['stream_id'].nunique().sort_values()

stream_count

valid_streamers = stream_count[stream_count >=2].index
valid_streamers

df = df[df['streamer_username'].isin(valid_streamers)]

#df.count()

#df.info()

#df.describe()

#df['streamer_username'].value_counts()

import matplotlib.pyplot as plt

data = df['streamer_username'].value_counts().values

# Plot histogram
plt.figure(figsize=(12, 6))
plt.hist(data, bins=150)

# Add labels and title
plt.title('Distribution of Streamer Username Frequencies', fontsize=16)
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(alpha=0.3)

# Show plot
#plt.show()



#graphing the top 10 streamer in a bar chart
plt.figure(figsize=(35,5))
df['streamer_username'].value_counts().head(50).plot(kind='bar')
# Add numbers (annotations) above each bar
for index, value in enumerate(df['streamer_username'].value_counts().head(50)):
    plt.text(index, value + 1, f'{value:.1f}', ha='center', va='bottom', fontsize=10)
plt.xticks(rotation=35)

df['total_time'] = df['time_stop'] - df['time_start']

df

df['total_time'].max()

df['total_time'].min()

#grouping by streamer name and getting average total time.
ave_watched_time = df.groupby('streamer_username')['total_time'].agg('mean').sort_values(ascending=False)

ave_watched_time

# Plotting the data as a bar chart
plt.figure(figsize=(20, 5))  # Adjust figure size
bar_chart = ave_watched_time.head(50).plot(kind='bar', color='skyblue')

# Add numbers (annotations) above each bar
for index, value in enumerate(ave_watched_time.head(50)):
    plt.text(index, value + 1, f'{value:.1f}', ha='center', va='bottom', fontsize=10)

# Customize the plot
plt.title("Top 50 Streamers by Average Watched Time", fontsize=16)
plt.xlabel("Streamer Username", fontsize=12)
plt.ylabel("Average Watched Time", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping

# Display the plot
#plt.show()

df

df = df.drop(columns=['time_start', 'time_stop','stream_id'])

#seeing how many unique streamer_username there are
df['streamer_username'].nunique()

df

from sklearn.neighbors import NearestNeighbors

df['streamer_username'].value_counts().sort_values(ascending=False)[:500]

top_1000 = df['streamer_username'].value_counts().sort_values(ascending=False)[:1000].index

top_1000

df[df['streamer_username'].isin(top_1000)]['user_id'].nunique()

df_1000 = df[df['streamer_username'].isin(top_1000)]

df_1000

um = df_1000.pivot_table(index="user_id", columns="streamer_username", values="total_time", aggfunc="max")

um

df_1000.describe()

um.isna().sum()

#item to item correlation
item_corr = um.corr()

item_corr

item_corr_imp = item_corr.fillna(0)

item_corr_imp

#creating knn model with um imputation with 0

nn = NearestNeighbors(n_neighbors=4)
nn.fit(item_corr_imp)

nn.kneighbors(item_corr_imp)
neighbors = nn.kneighbors(item_corr_imp, return_distance=False)

neighbors

def recommender_system(user_id,df, corrmat, neighbors, n):


  consumed = df.loc[df['user_id']==user_id, 'streamer_username'].unique()
  best_items = df.loc[(df['user_id']==user_id)].sort_values('total_time', ascending=False).drop_duplicates(subset='streamer_username')['streamer_username']

  best_list = []

  for item in best_items:
    idx = corrmat.index.get_loc(item)
    nearest = [corrmat.index[i] for i in neighbors[idx, 1:] if corrmat.index[i] not in consumed]
    best_list += list(nearest)

  return pd.Series(best_list).value_counts()[:n]

recommender_system(56,df_1000, item_corr_imp, neighbors,3)

from sklearn.metrics.pairwise import cosine_similarity

um_imp = um.fillna(0)

um_imp

items_sim = cosine_similarity(um_imp.T)

items_sim

item_sim = pd.DataFrame(items_sim, columns=um_imp.columns, index=um_imp.columns)
item_sim

nn_cos = NearestNeighbors(n_neighbors=4)
nn_cos.fit(item_sim)

neighbors_cos = nn_cos.kneighbors(item_sim, return_distance=False)
neighbors_cos

recommender_system(4,df_1000, item_sim, neighbors_cos,3)

um

um_imp

um_means = np.mean(um_imp, axis=1)
um_means

um_means.values.reshape(-1,1)

um_demeaned = um_imp - um_means.values.reshape(-1,1)

um_demeaned

r = np.linalg.matrix_rank(um_demeaned)

r

from scipy.sparse.linalg import svds

U, sigma, Vt = svds(um_demeaned.to_numpy(), k=400, random_state=42)

U.shape, sigma.shape, Vt.shape

um_repro = U@np.diag(sigma)@Vt

um_repro += um_means.values.reshape(-1,1)

um_imp
#rmse between the um_imp - repro

um_svd = pd.DataFrame(um_repro, index=um_imp.index, columns = um_imp.columns)

um_svd

#svd prediction using um_svd matrix
def predict_svd(user_id, df, um, n):
    consumed = df.loc[df['user_id']==user_id, 'streamer_username']
    user_streamers = um.loc[user_id,:]
    user_streamers = user_streamers.sort_values(ascending=False)
    user_streamer = user_streamers.drop(index=consumed)
    return user_streamer[:n]

predict_svd(1,df_1000, um_svd,3)

#rmse between the um_imp - um_svd
from sklearn.metrics import root_mean_squared_error
RMSE = root_mean_squared_error(um_imp,um_svd)
#print(f"The RMSE between the original model UM and SVD model UM is : {RMSE}")
print("Models completed! ")
print("")

flag = 'Y'
while(flag == 'Y'):
  user_input = int(input("1. Please enter a user id (1-1000): "))
  print(f"  You entered user id: {user_input}")
  print("")
  print(f"2. Your top three recommendations using cosine similary models: ")
  print("")
  print(f"{recommender_system(user_input,df_1000, item_sim, neighbors_cos,3)}")
  print("")
  print(f"3. Your top three recommendations svd model: ")
  print("")
  print(f"{predict_svd(user_input,df_1000, um_svd,3)}")
  print("")
  print(f"4. The RMSE between the original model UM and SVD model UM is : {RMSE}")
  print("")
  flag = input("Enter new user id? Press Y to run again: ")