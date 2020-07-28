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

由于数据维度太多，我们无法对数据进行可视化，所以选择用主成分分析法（Principal Components Analysis）对数据进行降维处理，在降维之前，我们需要对各个维度的数据进行标准化处理，以保证PCA的准确性

```python
x = np.array(rows)
scaler = StandardScaler()
X_train = scaler.fit_transform(x,)
pca = PCA(n_components=3, svd_solver='full', copy=True, whiten=True)
newX = pca.fit_transform(X_train)
print(pca.explained_variance_ratio_)
```

n_components=‘mle’意味着模型将根据计算结果自行选择最终维度，svd_solver=’full’意味着采取完全的奇异值分解，whiten=True意味着会将降维后的数据进行归一化处理，使得各维度方差相当。

通过可解释方差比重的结果我们发现，选取的第一个向量占据了51.6%的信息值，第二个向量占据了27.3%的信息值，第三个向量占据了15.1%的信息值，其余两个维度总计只占6%左右，所以我们选择舍弃调其他向量，仅保留这三个向量



### 聚类分析

得到了主向量之后，我们采用K-means算法进行聚类分析，采用了距离作为相似性的评价指标，认为两个对象的距离越近，其相似度越大。

为了选取合适的簇数量，我们在KmeansAssessment.py中采取了三种评价指标：inertia_，silhouette_score，calinski_harabasz_score。并绘制了当簇数目从3增加到8时，三项评价指标的走势图

![myplot1](C:\Users\hewenbing\Desktop\BigCode\pythonProgrammingHelper\QuestionDifficultyAssessment\plot\myplot1.png)

inertia是每个点到其簇的质心的距离之和，图形斜率越大，代表增加类别数量越能改善分类效果，inertia值越小，代表每个簇更加紧凑

从图中可以看出$k=4$和$k=5$的分类效果都还不错

![myplot2](C:\Users\hewenbing\Desktop\BigCode\pythonProgrammingHelper\QuestionDifficultyAssessment\plot\myplot2.png)

silhouette_score是轮廓系数，针对样本空间中的一个特定样本，计算它与所在聚类其它样本的平均距离a，以及该样本与距离最近的另一个聚类中所有样本的平均距离b，该样本的轮廓系数为(b-a)/max(a, b)，将整个样本空间中所有样本的轮廓系数取算数平均值，作为聚类划分的性能指标s。

轮廓系数的区间为：[-1, 1]。 -1代表分类效果差，1代表分类效果好。0代表聚类重叠，没有很好的划分聚类。因此从该图中我们可以看出$k=4$和$k=5$的聚类效果是比较好的。

![myplot3](C:\Users\hewenbing\Desktop\BigCode\pythonProgrammingHelper\QuestionDifficultyAssessment\plot\myplot3.png)

CH指标是通过计算类中各点与类中心的距离平方和来度量类内的紧密度，通过计算各类中心点与数据集中心点距离平方和来度量数据集的分离度，CH指标由分离度与紧密度的比值得到。从而，CH越大代表着类自身越紧密，类与类之间越分散，即更优的聚类结果。

从CH指标可以发现，$k=5$及之后的CH指标比较不错，但之前效果较好的$k=4$则一般



通过三张走势图的分析，我们可以发现当$k=5$时，能够在三项评价指标中都取得还不错的效果，因此最终我们设定簇的数量为5。

```python
kmeans = KMeans(n_clusters=5, copy_x=True).fit(newX)
```

然后将分类结果导入final.csv文件中，在classification列中列出了该题目所属类别，并对分类结果进行了可视化。

![myplot](C:\Users\hewenbing\Desktop\BigCode\pythonProgrammingHelper\QuestionDifficultyAssessment\plot\myplot.png)



### 评估结果

分类完成后，我们打开final.csv文件，通过classification我们可以观察到题目被分为了以下5类：

第0类：简单题，同学们面向用例的比例很小，并且代码复杂度也比较低，用例简单，大家提交次数都不多，得分都很高。一共有289道题目

第1类：中档题，虽然代码复杂低，但可能用例比较刁钻或者情景比较复杂，同学们的提交次数变得比较多（说明大家debug变困难了），但也侧面说明这一类题目是大家都在认认真真写的题目。这时已经有一部分同学开始感觉吃力因此选择面向用例的作弊手法了。

第2类：难题，由于题目比较难，同学们面向用例的比例大幅增加，此时差不多每道题都有超过2/3的同学选择了面向用例，但用例不太复杂，大家的代码复杂度也不高。我们推测应该是一些涉及到了高级的数据结构和算法的题目，过程并不复杂，但背后的原理比较困难。一部分同学选择自学后解决问题，剩下的同学就采取了面向用例的作弊方法。

第3类：也是难题，题目的逻辑相当复杂的题目，因此同学们的代码复杂度很高。这一类题目的得分情况相当极端，要么就几乎所有的同学都面向用例作弊了，要么就只有很少同学作弊。

第4类：奇葩题，因为分类显示这个类别下只有一道题，这道题大家的平均代码复杂度达到了惊人的55.5，因此我们单独提取出了这道题目，并检查了大家的代码，下面我们就来展示一下这道题目：

**题目描述**

将非负整数转换为其对应的英文表示。可以保证给定输入小于2<sup>31</sup> - 1 。

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> 1234567
<strong>输出:</strong> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"</pre>

```python
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
              'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        d2 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        if num == 0: return 'Zero'
        if num <= 20: return d1[num]
        if num < 100:
            t, d = num // 10, num % 10
            return d2[t] + ' ' + d1[d] if d > 0 else d2[t]

        if num < 1000:
            h = num // 100
            if num % 100 == 0: return d1[h] + ' Hundred'
            return d1[h] + ' Hundred ' + self.numberToWords(num % 100)

        if num < 10 ** 6:
            th = num // 10 ** 3
            if num % 10 ** 3 == 0:
                return self.numberToWords(th) + ' Thousand'
            return self.numberToWords(th) + ' Thousand ' + self.numberToWords(num % 10 ** 3)

        if num < 10 ** 9:
            mi = num // 10 ** 6
            if num % 10 ** 6 == 0:
                return self.numberToWords(mi) + ' Million'
            return self.numberToWords(mi) + ' Million ' + self.numberToWords(num % 10 ** 6)

        if num < 10 ** 12:
            bi = num // 10 ** 9
            if num % 10 ** 9 == 0:
                return d1[num // 10 ** 9] + ' Billion'
            return self.numberToWords(bi) + ' Billion ' + self.numberToWords(num % 10 ** 9)
a = input()
s = Solution()
print(s.numberToWords(int(a)))
```

从题目来看这应该是一道比较简单的题目才对，只需要利用表驱动进行简单地对应就可以进行转换了，为什么大家的复杂度如此之高呢？让我们来看一位同学的代码：

```python
str = int(input())

count = 0

answer = ""
while str >= 1000:
    part = ""
    left = str%1000
    lst = []
    str = int(str/1000)
    while left > 0:
        lefted = left % 10
        lst.insert(0, lefted)
        left = int(left / 10)
    if lst[0] == 1:
        part += "One Hundred "
    elif lst[0] == 2:
        part += "Two Hundred "
    elif lst[0] == 3:
        part += "Three Hundred "
    elif lst[0] == 4:
        part += "Four Hundred "
    elif lst[0] == 5:
        part += "Five Hundred "
    elif lst[0] == 6:
        part += "Six Hundred "
    elif lst[0] == 7:
        part += "Seven Hundred"
......
```

论文中我们只展示了代码的一小部分，但相信大家已经看明白了。这位同学一拿到题目就不考虑任何技巧，直接用if else来暴力解题以至于最终代码复杂度高达865.6！所以看来同学们的代码能力还是亟待提高，需要多多练习。



### 代码执行流程

1、先执行data_match.py文件，将两份源文件得到的题目分析数据进行匹配整理

2、再执行PCA.py文件，先对数据进行标准化处理，利用PCA进行降维，并进行KMeans聚类分析，得到题目难度分类结果和可视化图形，关于k值的选取，运用了inertia（肘部法则）、silhouette_score（轮廓系数）、calinski_harabasz_score（方差比准则）进行评估，选取最佳的k值



### 参考文件

sklearn文档

https://scikit-learn.org/stable/modules/classes.html

sklearn中PCA 参数的详细介绍

https://blog.csdn.net/guofei_fly/article/details/103956940

K-means聚类分析参数介绍

https://blog.csdn.net/github_39261590/article/details/76910689