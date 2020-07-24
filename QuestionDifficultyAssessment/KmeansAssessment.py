from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
class Assessment:

    def __init__(self, data):
        self.data = data

    def assessment(self):
        inertias = []
        silhouette = []
        calinski_harabasz = []
        for i in range(3, 8):
            kmeans = KMeans(n_clusters=i, copy_x=True).fit(self.data)
            inertias.append(kmeans.inertia_)
            silhouette.append(silhouette_score(self.data, kmeans.labels_))
            calinski_harabasz.append(calinski_harabasz_score(self.data, kmeans.labels_))
        plt.xlabel("k")
        plt.ylabel("inertia")
        X = range(3, 8)
        plt.plot(X, inertias, "o-")
        plt.show()
        plt.xlabel("k")
        plt.ylabel("silhouette_score")
        plt.plot(X, silhouette, "o-")
        plt.show()
        plt.xlabel("k")
        plt.ylabel("calinski_harabasz_score")
        plt.plot(X, calinski_harabasz, "o-")
        plt.show()

