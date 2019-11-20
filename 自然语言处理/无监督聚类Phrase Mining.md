# 文本聚类

## LDA模型( Latent Dirichlet Allocation )

LDA学习流程（Gibbs sampling）

+ 遍历所有文档中的每个词，随机分配一个topic

+ 对每个文档d：

  + 遍历d中的每个词w

    + （1）p(topic t | document d)：文档d中，话题为t的词的比例

      （2）p(word w | topic t)：话题t中，词w出现的比例

      按照概率p(t|d)*p(w|t)给词w分配一个新的话题。（根据生成式模型，这就是话题t产生词w的概率）

    + 换句话说，在这一步中我们假设，除了当前词以外，其他主题分配都是正确的，然后根据我们的生成模型更新当前词的话题。

+ 重复足够多次后，得到聚类结果。



参考：

[1] http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/

## Phrase Mining

（1）TopMine：频率模式挖掘+统计分析

（2）SegPhrase：弱监督、高质量的 Phrase Mining

（3）AutoPhrase：自动的 Phrase Mining



参考：

[1] https://zhuanlan.zhihu.com/p/34137119

[2] https://cci.drexel.edu/bigdata/bigdata2016/files/Keynote_Han.pdf

[3] http://elkishk2.web.engr.illinois.edu (Author of TopMine)

