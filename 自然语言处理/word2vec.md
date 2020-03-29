# word2vec

word2vec 分为 CBOW (Continuous Bag-of-Words) 与 Skip-Gram 两种模型。

CBOW 模型通过中心词的上下文来预测中心词的概率。Skip-Gram 模型和 CBOW 的思路是反着来的，即通过中心词来预测上下文词的概率。

CBOW 对小型数据库比较合适，而 Skip-Gram 在大型语料中表现更好。

##### CBOW (Continuous Bag-of-Words)模型

在神经网络语言模型中，词向量的表示学习只是为了建立语言模型得到的副产品。从 C&W 开始，就直接以生成词向量为目标构建模型了。

C&W 的基本思想是，给定训练语料中任意一个 n 元组（n=2C+1），如果把中心词随机替换成词表中别的词，那么真正的词一定比随机的词更合理，进行打分的话就是真实的中心词得分更高。训练过程就是拼接上下文词向量，然后送到隐藏层，最后经过线性变换得到一个分数。相比神经网络语言模型，最后一层计算量由 $O(|h|\times|V|)$ 下降到 $O(|h|)$。

CBOW 做了两点简化，一个是输入层不再拼接，而是取平均值，另外没有隐藏层，而是用 Logistic 回归计算中心词的概率。

首先随机初始化所有词向量 $e(w_i)$ 。给定一个 n 元组 $(w_i,C)=w_{i-C},...,w_{i-1},w_i,w_{i+1},...,w_{i+C}$ ，将上下文词 $WC=w_{i-C},...,w_{i-1},w_{i+1},...,w_{i+C}$ 的平均词向量作为输入：
$$
h=\frac1{2C}\sum_{i-C\le k\le i+C}e(w_k)
$$
中心词 $w_i$ 的概率为：
$$
P(w_i|WC)=\frac{\exp(h\cdot e(w_i))}{\sum_{k=1}^{|V|}\exp(h\cdot e(w_k))}
$$
训练时，对整个训练语料，优化词向量矩阵 $L$，最大化所有词的对数似然：
$$
L^*=\arg\max_L\sum_{w_i\in V}\log P(w_i|WC)
$$


##### Skip-gram 模型

给定一个 n 元组 $(w_i,C)$ ，利用中心词 $w_i$ 的词向量 $e(w_i)$ 预测上下文 $WC=w_{i-C},...,w_{i-1},w_{i+1},...,w_{i+C}$ 中每个词 $w_c$ 的概率：
$$
P(w_c|w_i)=\frac{\exp(e(w_i)\cdot e(w_c))}{\sum_{k=1}^{|V|}\exp(e(w_i)\cdot e(w_k))}
$$
目标函数与 CBOW 类似，优化词向量矩阵以最大化所有上下文词的对数似然：
$$
L^*=\arg\max_L\sum_{w_i\in V}\sum_{w_c\in WC}\log P(w_c|w_i)
$$

##### Hierarchical Softmax




##### 负采样

每个样本只更新一小部分权重，可以大大增加训练速度。



##### 参考：

[1] 通俗理解word2vec - 简书
https://www.jianshu.com/p/471d9bfbd72f

[2] word2vec 中的数学原理详解 - peghoty - 博客园
https://www.cnblogs.com/peghoty/p/3857839.html