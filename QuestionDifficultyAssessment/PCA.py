import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import csv
import pandas as pd

file3 = csv.reader(open('final.csv', 'r'))
rows = list(file3)
rows.remove(rows[0])
for i in range(len(rows)):
    rows[i] = rows[i][1:]
X = np.array(rows)
pca = PCA(n_components=2, svd_solver='full', copy=True, whiten=True)
newX = pca.fit_transform(X)

for i in range(len(newX)):
    plt.scatter(newX[i][0], newX[i][1])
plt.show()

# K-means cluster analysis

kmeans = KMeans(n_clusters=8, copy_x=True).fit_predict(newX)


data = pd.read_csv("final.csv")
data["classfication"] = kmeans
data.to_csv("final.csv", mode='w', index=False)

