### TODO

编程练习辅助系统

- 面向用例答案的过滤（已完成）

  - 直接对比输入和输出是否作为常量存储在代码中

- 代码复杂度分析（**秦锐鑫**）

  - 给出大概的复杂度（O(n),O(1),...）即可
  - 初步采用ppt中的比较准确的方法

- 代码片段推荐（选做）

- 相关题目推荐（**李淳**）

  - 题目的标签已经有了
  - $a_{ij}$表示第i个学生在第j类题目上取得的成绩
  - 推荐学生不擅长的题目提升

- 学生能力评估、题目难度评估（**何文兵**）

  - 评估维度有哪些？
  - 题目难度的评估维度：面向用例的学生比例、自定义的程序复杂度P（秦锐鑫）、该题目的最终成绩的平均提交得分（剔除面向用例的答案之后）、满分比例、提交次数
  - PCA之后得到重要的评估维度，进行K-means进行聚类分析，得到题目难度的几个档次
  - //每道题目给一个自定义编程能力得分$S_{ij}$（第i个学生在第j道题上的得分）= 题目难度*学生最终得分
  - //学生编程能力的评估维度：编程能力得分Score=$\sum{S}$、完成的题目数量
  - 高维的函数长什么样子？
  - 高维的函数plot可视化不出来，但是可以有三维和二维的，pca降维之后不一定能可视化
  - 学生能力需要符合多维正态分布（暂时不能确定）

- 如何使用上概率论中机器学习的部分

  - 题目推荐系统

  - 学生能力评估中利用PCA得到一些有趣的结果

    - > 相当于把数据变成线性无关的，去除相关性，并且可能发生了特征融合，所以出了一些新的特征，所以可能使结果变好。

    - 不过这样要求学生能力的刻画的维度要比较多，十个或以上比较好，不然没理由用PCA

- 系统整合（最后部分）

  - 每个模块的接口要设置好
  - 每个模块都有一个硬DDL
    - DDL 软 7.16 硬 7.18
  - 每三天开一次会



| 学生id | 题目id | 最终得分 | 是否面向用例 | 自定义程序复杂度P | 提交次数 | 题目难度 | 自定义得分S |
| ------ | ------ | -------- | ------------ | ----------------- | -------- | -------- | ----------- |
|        |        |          |              |                   |          |          |             |
|        |        |          |              |                   |          |          |             |
|        |        |          |              |                   |          |          |             |

| 学生   | 题目    | 最终得分 | 题目难度 |
| ------ | ------- | -------- | -------- |
| 何文兵 | 字符串1 | 100      | 简单     |
|        |         | 50       | 中等     |
|        |         | 100      | 困难     |

