# -*- coding: utf-8 -*-
"""dimensionality-reduction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fGOBEY5x0jSDT8PEXTJiHd3b33uu-zak
"""

import pandas as pd
import numpy as np

df  = pd.read_csv('/content/mnist.csv')

df

from sklearn.decomposition import PCA

data = df.drop(['label'],axis=1)
target = df['label']

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

data_scaled

pca = PCA(0.90)
pca.fit_transform(data_scaled)

pca.explained_variance_ratio_

pca.explained_variance_ratio_.sum()

pca.components_

print(f"Number of Components: {pca.n_components_}")