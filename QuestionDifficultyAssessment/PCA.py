import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2, copy=True, whiten=False)
newX = pca.fit_transform(X)
print(X)
print(newX)
print(pca.explained_variance_ratio_)

