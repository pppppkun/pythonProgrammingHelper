### 数据分析：

1、先执行data_match.py文件，将两份源文件得到的题目分析数据进行匹配整理

2、再执行PCA.py文件，利用PCA进行降维，并进行KMeans聚类分析，得到题目难度分类结果和可视化图形，关于k值的选取，运用了inertia（肘部法则）、silhouette_score（轮廓系数）、calinski_harabasz_score（方差比准则）进行评估，选取最佳的k值







### 参考文件：

sklearn文档

https://scikit-learn.org/stable/modules/classes.html

sklearn中PCA 参数的详细介绍

https://blog.csdn.net/guofei_fly/article/details/103956940

K-means聚类分析参数介绍

https://blog.csdn.net/github_39261590/article/details/76910689