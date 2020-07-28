import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
import pandas as pd
import KmeansAssessment

file3 = csv.reader(open('final.csv', 'r'))
rows = list(file3)
rows.remove(rows[0])
for i in range(len(rows)):
    rows[i] = rows[i][1:]
x = np.array(rows)
scaler = StandardScaler()
X_train = scaler.fit_transform(x,)
pca = PCA(n_components=3, svd_solver='full', copy=True, whiten=True)
newX = pca.fit_transform(X_train)
print(pca.explained_variance_ratio_)

# K-means cluster analysis
#k = KmeansAssessment.Assessment(newX)
#k.assessment()

kmeans = KMeans(n_clusters=4, copy_x=True).fit(newX)
print(kmeans.cluster_centers_)
print(kmeans.inertia_)
fig = plt.figure()
ax = Axes3D(fig)
for i in range(len(newX)):
    if kmeans.labels_[i] == 0:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="blue")
    elif kmeans.labels_[i] == 1:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="red")
    elif kmeans.labels_[i] == 2:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="yellow")
    elif kmeans.labels_[i] == 3:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="green")
    elif kmeans.labels_[i] == 4:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="purple")
    elif kmeans.labels_[i] == 5:
        ax.scatter(newX[i][0], newX[i][1], newX[i][2], c="black")
plt.show()

data = pd.read_csv("final.csv")
data["classification"] = kmeans.labels_
data.to_csv("final.csv", mode='w', index=False)

