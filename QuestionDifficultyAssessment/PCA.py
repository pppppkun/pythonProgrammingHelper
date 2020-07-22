import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import csv

file3 = csv.reader(open('final.csv', 'r'))
rows = list(file3)
rows.remove(rows[0])
for i in range(len(rows)):
    rows[i] = rows[i][1:]
X = np.array(rows)
pca = PCA(n_components=3, copy=True, whiten=True)
newX = pca.fit_transform(X)
print(newX)
print(pca.explained_variance_ratio_)
#print(pca.score_samples(X))
#for i in range(6):
    #plt.scatter(newX[i, 0], newX[i, 1], alpha=0.8)
#plt.show()

#[0.77747542 0.2192404 ]