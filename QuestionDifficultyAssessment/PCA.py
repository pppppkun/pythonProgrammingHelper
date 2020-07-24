import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import csv
import pandas as pd
import KmeansAssessment

file3 = csv.reader(open('final.csv', 'r'))
rows = list(file3)
rows.remove(rows[0])
for i in range(len(rows)):
    rows[i] = rows[i][1:]
X = np.array(rows)
pca = PCA(n_components=2, svd_solver='full', copy=True, whiten=True)
newX = pca.fit_transform(X)


# K-means cluster analysis
k = KmeansAssessment.Assessment(newX)
k.assessment()

kmeans = KMeans(n_clusters=6, copy_x=True).fit(newX)
print(kmeans.cluster_centers_)
print(kmeans.inertia_)
for i in range(len(newX)):
    if kmeans.labels_[i] == 0:
        plt.scatter(newX[i][0], newX[i][1], c="blue")
    elif kmeans.labels_[i] == 1:
        plt.scatter(newX[i][0], newX[i][1], c="red")
    elif kmeans.labels_[i] == 2:
        plt.scatter(newX[i][0], newX[i][1], c="yellow")
    elif kmeans.labels_[i] == 3:
        plt.scatter(newX[i][0], newX[i][1], c="green")
    elif kmeans.labels_[i] == 4:
        plt.scatter(newX[i][0], newX[i][1], c="purple")
    elif kmeans.labels_[i] == 5:
        plt.scatter(newX[i][0], newX[i][1], c="black")
plt.show()

data = pd.read_csv("final.csv")
data["classfication"] = kmeans.labels_
data.to_csv("final.csv", mode='w', index=False)

