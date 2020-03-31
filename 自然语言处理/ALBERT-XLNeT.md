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



**参考：** 蓝振忠的直播课程：https://www.bilibili.com/video/BV1C7411c7Ag?p=4



# XLNeT

### 自回归与自编码

大家通常说的语言模型是根据上文内容预测下一个可能的单词，这种单向的语言模型被称为自回归语言模型（Autoregressive LM）。与之相对的，像 BERT 这种在输入 X 中随机 Mask 掉一部分单词，并用上下文进行预测的语言模型被称为自编码语言模型（Autoencoding LM）。

自回归语言模型比较适合生成问题，缺点是不能同时利用上下文信息。

自编码语言模型虽然能利用上下文，但由于引入了 [Mask] 标记，导致了预训练阶段和 Fine-tuning 阶段的数据不一致，也就是引入了噪音，即 DAE（Denoising Autoencoder）。另外 BERT 假设不同的 [Mask] 相互独立，忽略了 [Mask] 之间的关联性。



### XLNet如何解决这些问题？

##### 置换语言模型（Permutation LM）

把单词顺序打乱，当预测某个词的时候，句子里的其他词都有可能成为上文。

这样看上去还是自回归语言模型，但同时包含了上文和下文信息。

##### 双流注意力

要实现上面的想法，实际上并不是真的把原始数据进行排列组合再采样，而是使用了双流 Attention 掩码机制。

假设当前要预测第 i 个词，通过 Attention 掩码，从其他词里随机选择 i-1 个放到上文中，把其他单词 Mask 掉。

双流注意力机制包括 **内容流** 和 **Query流** ，其中内容流就是标准的 Transformer 计算过程，而 Query流 用来代替 BERT 的 [Mask] 标记。由于输入时不能看到被预测的单词，Query流忽略掉这个词的输入，只保留了位置信息。



##### Transformer-XL

BERT 的序列长度是固定的，当遇到长序列时，通常需要拆成 sentence 级别的短序列，这样割裂了短序列之间的联系。Transformer-XL 的做法是把上一个短序列的各层输入的一部分作为 memory 缓存，和当前各层的输入拼接，以获取上文信息。



##### 参考：

[1] XLNet原理浅析 - 知乎
https://zhuanlan.zhihu.com/p/70395238

[2] XLNet:运行机制及和Bert的异同比较 - 知乎
https://zhuanlan.zhihu.com/p/70257427