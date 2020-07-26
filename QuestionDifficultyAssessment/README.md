# 题目难度评估模块

### 简介

在之前的模块中我们获得了一些统计数据，例如学生在该题目上的最终代码的程序复杂度、该题目采取面向用例的学生比例，该题目的学生平均得分，该题目的平均提交次数等等。于是在这个模块中我们尝试利用这些数据维度来评估一道题目在同学们心中的难度如何。



### 数据匹配

data_match.py文件对两份数据文件csv_test_by_pkun.csv和csv_test_by_Qin.py进行匹配整理，最终得到了600多道题目统计数据，并导入了final.csv。

final.csv文件的格式如下:

| case_id | case_oriented_ratio | final_average_score | full_score_ratio | upload_times | average_complexity | classification |
| ------- | ------------------- | ------------------- | ---------------- | ------------ | ------------------ | -------------- |
|         |                     |                     |                  |              |                    |                |

[^notice]: 其中所有面向用例的提交，我们均视为同学作弊，在统计时最终成绩计为0分。



### 主成分分析法降维

由于数据维度太多，我们无法对数据进行可视化，所以选择用主成分分析法（Principal Components Analysis）对数据进行降维处理

```python
pca = PCA(n_components='mle', svd_solver='full', copy=True, whiten=True)
newX = pca.fit_transform(X)
print(pca.explained_variance_ratio_)
```

n_components=‘mle’意味着模型将根据计算结果自行选择最终维度，svd_solver=’full’意味着采取完全的奇异值分解，whiten=True意味着会将降维后的数据进行归一化处理，使得各维度方差相当。

通过可解释方差比重的结果我们发现，选取的第一个向量占据了84%的信息值，第二个向量占据了15.5%的信息值，所以我们选择舍弃调其他向量，仅保留这两个向量



### 聚类分析

得到了主向量之后，我们采用K-means算法进行聚类分析，采用了距离作为相似性的评价指标，认为两个对象的距离越近，其相似度越大。

为了选取合适的簇数量，我们在KmeansAssessment.py中采取了三种评价指标：inertia_，silhouette_score，calinski_harabasz_score。并绘制了当簇数目从3增加到8时，三项评价指标的走势图

![myplot1](C:\Users\hewenbing\Desktop\myplot1.png)

inertia是每个点到其簇的质心的距离之和，图形斜率越大，代表增加类别数量越能改善分类效果

从图中可以看出$k=6$之后的分类效果变化不明显

![myplot2](C:\Users\hewenbing\Desktop\myplot2.png)

silhouette_score是轮廓系数，针对样本空间中的一个特定样本，计算它与所在聚类其它样本的平均距离a，以及该样本与距离最近的另一个聚类中所有样本的平均距离b，该样本的轮廓系数为(b-a)/max(a, b)，将整个样本空间中所有样本的轮廓系数取算数平均值，作为聚类划分的性能指标s。             轮廓系数的区间为：[-1, 1]。 -1代表分类效果差，1代表分类效果好。0代表聚类重叠，没有很好的划分聚类。

![myplot3](C:\Users\hewenbing\Desktop\myplot3.png)

CH指标是通过计算类中各点与类中心的距离平方和来度量类内的紧密度，通过计算各类中心点与数据集中心点距离平方和来度量数据集的分离度，CH指标由分离度与紧密度的比值得到。从而，CH越大代表着类自身越紧密，类与类之间越分散，即更优的聚类结果。



通过三张走势图的分析，我们可以发现当$k=6$时，能够在三项评价指标中都取得还不错的效果，因此最终我们设定簇的数量为6。

```python
kmeans = KMeans(n_clusters=6, copy_x=True).fit(newX)
```

然后将分类结果导入final.csv文件中，在classification列中列出了该题目所属类别，并对分类结果进行了可视化。

![myplot4](C:\Users\hewenbing\Desktop\myplot4.png)



### 代码执行流程

1、先执行data_match.py文件，将两份源文件得到的题目分析数据进行匹配整理

2、再执行PCA.py文件，利用PCA进行降维，并进行KMeans聚类分析，得到题目难度分类结果和可视化图形，关于k值的选取，运用了inertia（肘部法则）、silhouette_score（轮廓系数）、calinski_harabasz_score（方差比准则）进行评估，选取最佳的k值



### 参考文件

sklearn文档

https://scikit-learn.org/stable/modules/classes.html

sklearn中PCA 参数的详细介绍

https://blog.csdn.net/guofei_fly/article/details/103956940

K-means聚类分析参数介绍

https://blog.csdn.net/github_39261590/article/details/76910689