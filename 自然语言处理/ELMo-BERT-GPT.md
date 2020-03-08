## ELMo

双向 + BiLSTM

ELMO使用两层 BiLSTM 网络进行训练，两个方向的隐藏层向量拼接起来进入下一层。

最后得到的词向量是三层向量（嵌入层和两个BiLSTM层）加权求和。



## BERT

双向 + transfomer

##### Embedding

Bert 的词嵌入由三种 embedding 求和得到。

+ Token embedding：词向量，第一个单词是 [CLS] 标志，可以用于之后的分类任务
+ Segment embedding：文本向量，用来刻画文本的全局语义信息
+ Position embedding：位置向量，对不同位置的词附加一个不同的向量加以区分



##### 预训练1：Masked LM (Language Model)

为了解决双向语言模型 “自己看见自己” 的问题，BERT使用了 [Mask] 方法。

在一句话中随机抹去 15%的词用于预测，而不是像 CBOW 一样把每个词都预测一遍。

由于这个操作会导致 pre-training 和 fine-tuning 的不一致，对于被抹去的词，80%用一个特殊符号 [MASK] 替换，10%用一个任意词替换，剩下10%保持不变。

步骤：

1. 在encoder的输出上添加一个分类层
2. 用嵌入矩阵乘以输出向量，将其转换为词汇的维度
3. 用 Softmax 计算词汇表中每个单词的概率

由于一次只预测15%，所以收敛比较慢。



##### 预训练2：Next sentence prediction

在训练过程中，接收成对的句子作为输入，并预测第二个句子是否在原始文档中也是后续句子。训练期间，50%的输入在原始文档中是前后关系，另外50%是从语料库中随机组成的，并且是与第一句断开的。

为了区分这两个句子，输入在进入模型之前要做以下处理：

1. 在第一个句子开头插入 [CLS] ，在末尾插入 [SEP]
2. 将表示句子的embedding（文本向量）添加到每个词token上
3. 给每个token添加一个位置embedding，来表示它在序列中的位置。

预测时用一个分类层将 [CLS] 标记的输出变换为 2*1 形状的向量，用 Softmax 计算概率。



训练BERT模型时，Masked LM 和 Next Sentence Prediction 一起训练，目标是最小化两种策略的组合损失函数。



##### Encoder

使用transformer encoder进行特征提取。作者分别用12层和24层encoder组装了两套BERT模型，参数分别为 110M 和 340M。





## GPT/GPT-2

单向 + transformer，对 transformer 结构做了调整。

GPT-2 超大参数量 1542M（ELMo 94M，BERT 340M）

使用单向语言模型，即 Decoder 的 Masked Multi-Head Attention，保留了根据上文生成下文的能力，原始的BERT并不具备。



参考：

[1] 图解BERT模型：从零开始构建BERT - 云+社区 - 腾讯云
https://cloud.tencent.com/developer/article/1389555

[2] Language Models and Contextualised Word Embeddings
http://www.davidsbatista.net/blog/2018/12/06/Word_Embeddings/

[3] 从语言模型看Bert的善变与GPT的坚守 - 云+社区 - 腾讯云
https://cloud.tencent.com/developer/article/1429585

[4] NLP——GPT对比GPT-2 - 知乎
https://zhuanlan.zhihu.com/p/96791725?from_voters_page=true

[5] 李宏毅-ELMO, BERT, GPT讲解_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili
https://www.bilibili.com/video/av56235038/?spm_id_from=333.788.videocard.4