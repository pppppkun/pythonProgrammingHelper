import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

X = np.array([[-1, -1, -5], [-2, -1, 5], [-3, -2, -5], [1, 1, -5], [2, 1, 5], [3, 2, 5]])
pca = PCA(n_components=3, copy=True, whiten=False)
newX = pca.fit_transform(X)
print(X)
print(newX)
print(pca.explained_variance_ratio_)
print(pca.score_samples(X))
for i in range(6):
    plt.scatter(newX[i, 0], newX[i, 1], alpha=0.8)
plt.show()

#[0.77747542 0.2192404 ]