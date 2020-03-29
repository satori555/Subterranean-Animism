# word2vec

Word2vec 分为 CBOW (Continuous Bag-of-Words) 与 Skip-Gram 两种模型。

CBOW 是 C&W 模型的一个改进版，基本思想是通过中心词的上下文来预测中心词的概率。

在神经网络语言模型中，词向量的表示学习只是为了建立语言模型得到的副产品。从 C&W 开始，就直接以生成词向量为目标构建模型了。

C&W 的基本思想是，给定训练语料中任意一个 $n$ 元组（$n=2C+1$），如果把中心词随机替换成词表中别的词，那么真正的词一定比随机的词更合理，进行打分的话就是真实的中心词得分更高。训练过程就是拼接上下文词向量，然后送到隐藏层，最后经过线性变换得到一个分数。相比神经网络语言模型，最后一层计算量由 $O(|h|\times|V|)$ 下降到 $O(|h|)$ 。

相比于 C&W 模型，CBOW 做了两点简化，一个是上下文词向量不再拼接，而是取平均值，另外没有隐藏层，而是用 Logistic 回归计算中心词的概率。

Skip-Gram 模型和 CBOW 的思路是反着来的，即通过中心词来预测上下文词的概率。

CBOW 对小型数据集比较合适，而 Skip-Gram 在大型语料中表现更好。



### CBOW (Continuous Bag-of-Words)模型

首先初始化词向量，即随机生成一个词 embedding 矩阵 V，用 one-hot 向量和 embedding 矩阵相乘，就得到一个词向量。另外再生成一个相同维度的 context 矩阵 U，是为了方便推导。对于词表 D 中的每一个词，我们通过点乘计算它和所有 context 向量的相似度：$u^Tv$ ，然后通过 softmax 映射到 0-1 表示概率，也可以用logistic 回归计算概率。

对于中心词 $w_i$ ，上下文词 $\{w_{i-C},...,w_{i-1},w_{i+1},...,w_{i+C}\}$ 的平均词向量为：
$$
x_i=\frac1{2C}\sum_{-C\le j\le C}v(w_{i+j})
$$
中心词 $w_i$ 的概率为：
$$
p(w_i|\text{context}_i)=\frac{\exp(u_i^T x_i)}{\sum_{k\in D}\exp(u_k^T x_i)}
$$
我们希望对于目标词这个条件概率为 1 ，对于其他词条件概率为 0 。

目标函数为所有位置预测结果的乘积：
$$
\prod_{i\in D}p(w_i|\text{context}_i,\theta)
$$
其中参数 $\theta$ 就是所有词的向量表示，即矩阵 V 和 U。

取负对数得到损失函数：
$$
L(\theta)=-\sum_{i\in D} \log p(w_i|\text{context}_i,\theta)
$$
损失函数分别对 $u,v$ 求导，用梯度下降法更新参数。



##### Skip-gram 模型

Ship-gram 的目的是通过中心词来预测上下文词出现的概率，推导过程和 CBOW 基本是一样的。

首先同样初始化 embedding 矩阵 V 和 context 矩阵 U。记中心词为 $w_c$ ，要预测的上下文词为 $w_o$ ，用向量内积表示相似度，条件概率为
$$
p(w_o|w_c)=\frac{\exp(u_o^Tv_c)}{\sum_{k\in D}\exp(u_k^Tv_c)}
$$
我们希望对于目标词这个条件概率为 1 ，对于其他词条件概率为 0 。

目标函数为所有位置预测结果的乘积：
$$
\prod_{i\in D}\prod_{-C\le j\le C}p(w_{i+j}|w_i,\theta)
$$
取负对数得到损失函数：
$$
L(\theta)=-\sum_{i\in D}\sum_{-C\le j\le C} \log p(w_{i+j}|w_i,\theta)
$$
损失函数分别对 $u,v$ 求导，用梯度下降法更新参数。



##### Hierarchical Softmax

Hierarchical Softmax 是 word2vec 中提高性能的一项关键技术，输出层使用了 Huffman 树，每次分支都是一个二分类问题，我们用 $d\in\{0,1\}$ 表示每一级的 Huffman 编码。

根据逻辑回归，一个节点被分为正类（d=1）的概率为
$$
\sigma(x^T\theta)=\frac1{1+e^{-x^T\theta}}
$$
被分为负类（d=0）的概率即为
$$
1-\sigma(x^T\theta)
$$
首先我们对词表中的所有词建立一棵 Huffman 树，每个叶子节点对应一个辅助向量 $\theta$，同时每个非叶子节点也有一个等长的辅助向量。

例如对于 CBOW 模型，我们想预测 “足球” 这个词，它的 Huffman 编码为 `1001` 。设上下文平均词向量为 $x$，从根节点出发到达 “足球” 需要经历 4 次二分类：

+ 第 1 次： $p(d_2|x,\theta_1)=\sigma(x^T\theta_1)$ 
+ 第 2 次： $p(d_3|x,\theta_2)=1-\sigma(x^T\theta_2)$ 
+ 第 3 次： $p(d_4|x,\theta_3)=1-\sigma(x^T\theta_3)$ 
+ 第 4 次： $p(d_5|x,\theta_4)=\sigma(x^T\theta_4)$ 

我们想求的条件概率即为：
$$
p(足球|context)=\prod_{j=2}^5p(d_j|x,\theta_{j-1})
$$
对于词表中的任意一个词，Huffman 树中必存在一条从根节点到这个词的路径，把每个分支看作二分类，把每次分类的概率连乘起来得到最后的条件概率。每一级的条件概率为：
$$
p(d_j|x,\theta_{j-1})=[\sigma(x,\theta_{j-1})]^{d_j}\cdot[1-\sigma(x,\theta_{j-1})]^{1-d_j}
$$
然后得到对数似然函数 $L(w,j),w\in D$，分别对 $\theta_j^w$ 和 $x_w$ 求导计算参数。

对于词向量 $v$ 的更新，直接用 $x$ 的结果：
$$
v(w')=v(w')+\eta\sum_j\frac{\part L(w,j)}{\part x_w},w'\in\text{context}(w)
$$
对于 Skip-gram 模型的推导是类似的。




##### 负采样

每次更新时，除了目标词为正样本，其他所有词都是负样本。实际上不用每次都更新全部负样本，只选择一小部分进行更新效果也很好，这样就可以大大增加训练速度。

负样本的选择可以有多种方法，一般来说，高频词被选为负样本的概率更大。



##### 参考：

[1] word2vec 中的数学原理详解 - peghoty - 博客园
https://www.cnblogs.com/peghoty/p/3857839.html
