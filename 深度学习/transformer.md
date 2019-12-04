# Transformer

### 网络结构

input -> encoder -> decoder -> output

encoder和decoder各有6层。（补充图）

### Encoder

每个encoder包含Self-Attention和Feed Forword NN两层。



### Positional Encoding

考虑输入序列的位置信息，实际的输入序列是embedding加上一个位置编码（positional encoding）。论文中使用三角函数生成位置编码。

在decoder的最底层也要输入相对应的位置编码。



### Self-Attention

Embedding: dim = 512

sequence lengths: seq = 2

Attention vectors: Q, K, V, size = (64 * seq)

参数：Wq, Wk, Wv, size = (64 * dim)
$$
Attention(Q,K,V)=Softmax\left( \frac{QK^T}{\sqrt{64}} \right)V
$$

### Multi-Head Attention:

使用8个Attention，拼接起来，size = (512 * seq). (512 = 8 * 64)

权重参数Wo，size = (dim * 512)

输出Z矩阵，size = (dim, seq)



### Residues and Layer Normalization

Add：$x_i$为embedding加positional encoding，$z_i$为self-attention层的输出。实际上进入全连接层的是经过Layer Nornalization的$x_i+z_i$。

Normalize：对每一层所有神经元上的数据做normalization（不考虑batch）。

比较：batch normalization是对每个神经元上的一个batch的数据做normalization。

### Decoder



## 参考资料：

[1] https://arxiv.org/abs/1706.03762

[2] https://jalammar.github.io/illustrated-transformer/

[3] https://www.jianshu.com/p/c94909b835d6