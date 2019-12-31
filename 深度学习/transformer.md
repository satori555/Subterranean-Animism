# Transformer

### 网络结构

输入 -> 6层encoder -> 6层decoder -> 输出

### Encoder

每个encoder包含Self-Attention和Feed Forword NN两层。

### Positional Encoding

考虑输入序列的位置信息，实际的输入序列是embedding加上一个位置编码（positional encoding）。论文中使用三角函数生成位置编码。

在decoder的最底层也要输入相对应的位置编码。

### Self-Attention

词嵌入Embedding维度为dim（下图中dim=4），句子长度seq，输入矩阵X，shape(seq, dim) 

Query, Key and Value matrices: Q, K, V, shape(seq, 64)。64为QKV向量的维度，下图中为3。

计算矩阵Q: $XW_q=Q$，计算K和V方法类似。参数：Wq, Wk, Wv, shape(dim, 64)

注意力计算：
$$
Attention(Q,K,V)=Softmax\left( \frac{QK^T}{\sqrt{64}} \right)V
$$

如图，输出Z即为Attention，shape(seq, 64)：

![transformer1](D:\Users\test\Documents\GitHub\Subterranean-Animism\image_storage\transformer1.png)



### Multi-Head Attention:

Transformer使用了8个Attention，单个Attention的shape为(seq, 64)，8个拼起来shape(seq, 512)

现在我们想把Attention的shape变为和输入X一致，加入一个权重矩阵Wo，shape(512, dim)，让Attention矩阵和Wo矩阵相乘，得到Z矩阵，shape(seq, dim)，和X一致。

整个计算Attention的流程如图：

![transformer_multi-headed_self-attention-recap](..\image_storage\transformer2.png)



### Residues and Layer Normalization

Add (redisual connection)：X为embedding加positional encoding，Z为self-attention层的输出。实际上进入全连接层的是经过Layer Nornalization的X+Z。

Normalize：对每一层所有神经元上的数据做normalization（不考虑batch）。

比较：batch normalization是对每个神经元上的一个batch的数据做normalization。batch和layer normalization可以看作在两个互相垂直的维度上做归一化。

### Decoder

每一层decoder包含两级Attention。

第一级Masked Multi-head Attention加入了Mask操作，即我们只能attend到前面已经翻译过的输出词语，后面的词语被覆盖掉了（通过设置相应的positional encoding为-inf）

第二级encoder-decoder attention，它的Q来自前一级decoder层的输出，但K和V来自encoder，这使得decoder的每个位置都可以attend到输入序列的每一个位置。

整个流程如图：

![transformer_resideual_layer_norm_3](../image_storage/transformer3.png)





## 参考资料：

[1] https://arxiv.org/abs/1706.03762

[2] https://jalammar.github.io/illustrated-transformer/

