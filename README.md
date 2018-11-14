# NaiveBayes
Spam email classifier using Naive Bayes method.

The 2th project of AI course.

## 实验内容

根据Naive Bayes模型，使用不同长度的训练集对字典进行训练，再使用训练后的字典对测试集进行垃圾邮件分类，最后进行不同长度训练集下的误差分析。

**选用的数据集:**

![](https://i.imgur.com/3Ws4nZ4.png)

**训练数据:**

train-features-* 为训练邮件，分别包含50，100，400，700封邮件。
其中所有邮件经过预处理，对于每一个单词给出“所属邮件编号，字典中编号，出现次数”。

train-labels-* 为训练邮件标识，内包含对应训练邮件是否为垃圾邮件的标识，0为正常邮件，1为垃圾邮件。

**测试数据:**

test-features 为测试邮件。

test-labels 为测试邮件标识。

**分类模型:**

朴素贝叶斯(Naive Bayes)分类器
> 朴素贝叶斯分类器基于一个简单的假定：给定目标值时属性之间相互条件独立。
**P( Category | Document) = P ( Document | Category ) * P( Category) / P(Document)**

## 训练过程

对于训练过程，有：
![](https://i.imgur.com/FDi0oeg.png)

其中，
φk|y=1表示字典中第k个单词在垃圾邮件中出现的概率
φk|y=0表示字典中第k个单词在正常邮件中出现的概率
φy表示该邮件是垃圾邮件的概率

m为训练集邮件数
V为字典长度

**训练目标：计算字典中所有单词的 φk|y=1, φk|y=0, φy**

## 测试过程

对于测试集，判断测试邮件是否为垃圾邮件，有：
![](https://i.imgur.com/7jcX3Mp.png)

如果不等式成立，则该邮件为垃圾邮件。
 
## 结果

50封的测试结果

![](https://i.imgur.com/8sY77qm.png)

matlab结果

![](https://i.imgur.com/4krXesi.png)

100封的测试结果

![](https://i.imgur.com/UwNQVcj.png)

matlab结果

![](https://i.imgur.com/eqM7Exr.png)

400封的测试结果

![](https://i.imgur.com/UwNQVcj.png)

matlab结果

![](https://i.imgur.com/eqM7Exr.png)

700封的测试结果

![](https://i.imgur.com/CScSRFI.png)

matlab结果

![](https://i.imgur.com/Bco7jd5.png)
