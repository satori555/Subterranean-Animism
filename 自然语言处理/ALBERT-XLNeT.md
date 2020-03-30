# ALBERT

BERT 模型可以进一步增大宽度得到更好的效果，但参数量过大使得计算难以进行。

### 如何减少参数数量？

##### Method 1: factorized embedding parametrization. 

+ Token embeddings are context independent while hidden layer embeddings are context dependent.
+ Token embeddings are sparsely updated.

解释：BERT 的第一步是从 one-hot 到 embedding 的全连接层，设词表大小为 V， embedding 维度为 H，那么这一层需要的参数量为 O(V * H)。由于 one-hot 绝大多数值为 0，而且此时词与词之间是没有交互的，不需要很大的维度就可以表示它们，因此可以先把 one-hot 映射到一个很低的维度 E，再升高到我们需要的维度 H。

参数量：O(V * H) -> O(V * E + E * H), where E << H

##### Method 2: cross-leyer parameter sharing. 

+ The attention-feedforward operations are repeated, can we share their parameters?
+ Visualizations of attention map show similar operation across layers.

解释：从图形化显示可以看出，每一层的 attention-feedforward 参数是相似的，因此可以尝试使用参数共享，参数量最多可以减少到原来的 1/L，L 为层数。从测试结果可以看出，大多数 performance drop 来自于 FFN 层的参数共享。由于 attention 层的参数更多，最后选择全部共享以尽可能压缩参数。

参数量：O(12 * L * H * H) -> O(12 * H * H) 

### 结果

使用以上两个 method，就可以进一步把 BERT 变宽、变深。

宽度：一个 ALBERT-xxlarge 模型宽度（4096）是 BERT-large 的四倍（1024），但只需要 70% 的参数量。平均表现提升了 3.5%，但训练速度变慢了 3 倍，这个问题扔有待于解决。

深度：ALBERT-large 12 层和 24 层表现差不多，而从 24 层提高到 48 层结果反而变差了。

### 其他提高

预训练：NSP -> SOP (sentence order prediction)

MLM (musked language model) 几乎不会过拟合，因此可以去掉 dropout 以提高 capacity。

增加了 10 倍以上的训练数据。



**参考：** 原作者蓝振忠的直播课程：https://www.bilibili.com/video/BV1C7411c7Ag?p=4



# XLNeT

自回归与自编码。

排列组合序列：解决上下文预测问题。

双流注意力：解决位置信息缺失问题。

Transformer-XL：长序列。



##### 参考：

[1] XLNet原理浅析 - 知乎
https://zhuanlan.zhihu.com/p/70395238

[2] XLNet:运行机制及和Bert的异同比较 - 知乎
https://zhuanlan.zhihu.com/p/70257427