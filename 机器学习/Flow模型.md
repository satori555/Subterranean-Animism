# Flow模型

生成模型除了GAN和VAE，还有基于flow的模型。

生成模型的本质，是希望用一个我们知道的概率模型来拟合数据样本 $X$，也就是想写出一个带参数 $\theta$ 的分布 $p_X(x,\theta)$ 。神经网络可以拟合任意函数，却不能拟合任意概率分布。

在flow模型中，我们尝试寻找一个可逆变换 $z=f(x)$ ，新的变量服从一个简单的分布（如高斯分布），这两个分布的关系为：
$$
p_X(x)=p_Z(f(x))|\det \frac{\part f(x)}{\part x}|
$$
得到变换关系 $f(x)$ 之后我们就可以从简单的 $Z$ 的分布中采样，然后通过变换生成 $X$ 。

函数 $f(x)$ 需要满足两个要求：可逆、雅可比行列式易于计算。



### NICE: Non-linear Independent Components Estimation

由于三角阵的行列式最容易计算，我们可以想办法使变换 $f(x)$ 的雅可比矩阵为三角阵。在NICE中，输入数据 $x$ 被拆分成两部分 $x_1,x_2$，然后做变换：
$$
h_1=x_1 \\
h_2=x_2+m(x_1)
$$
其中 $x_1$ 和 $x_2$ 是 $x$ 的某种划分，$m$ 是 $x_1$ 的任意函数。这一层被称为 **加性耦合层（Additive coupling）**。

这个变换的雅可比矩阵是一个三角阵，而且对角线元素都是 1：
$$
\frac{\part h}{\part x} = \left (
\begin{matrix}
I_{1:d} & O \\
\frac{\part m}{\part x_1} & I_{d+1:D}
\end{matrix}
\right )
$$
其逆变换为：
$$
x_1=h_1 \\
x_2=h_2-m(h_1)
$$
由于这个变换的一部分是恒等变换，为了增强拟合能力我们需要叠加多个耦合层：
$$
x=h^{(0)}\Leftrightarrow h^{(1)}\Leftrightarrow h^{(2)}\Leftrightarrow 
\cdots\Leftrightarrow h^{(n)} =z
$$
每一层的行列式都是 1 。

要注意如果耦合的顺序一直保持不变，那么第一部分依然是平凡的。可以考虑在每次加性耦合之前，打乱或者反转输入的各个维度的顺序，或简单地交换这两部分的位置，使信息可以充分混合。



此外还有尺度变化和特征解耦等。



### Real NVP：real-valued non-volume preserving transformations





**参考：**

[1] 细水长flow之NICE：流模型的基本概念与实现
https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247490842&idx=1&sn=840d5d8038cd923af827eef497e71404&chksm=96e9c29aa19e4b8c45980b39eb28d80408632c8f9a570c9413748b2b5699260190e0d7b4ed16&scene=21#wechat_redirect

[2] 流模型之NICE - 知乎
https://zhuanlan.zhihu.com/p/45523924

[3] 流模型之RealNVP - 知乎
https://zhuanlan.zhihu.com/p/46107505

[4] RealNVP与Glow：流模型的传承与升华 | 机器之心
https://www.jiqizhixin.com/articles/2018-08-27-9