# Recurrent Neural Networks (RNN)

### 定义

网络结构如图：

![6e28bccb944dba0c7e6c5b9ead7e144c_rnn](D:\Users\test\Documents\笔记\RNN.assets\6e28bccb944dba0c7e6c5b9ead7e144c_rnn.jpg)



不多解释，直接上公式：
$$
s_t = \tanh(Ux_t + W s_{t-1})\\
\hat y = softmax(Vs_{t-1})
$$
其中 $U, W, V$ 为待确定的权重（矩阵），$x_t, s_t, \hat y_t$都是向量，偏置参数在这里先忽略。

误差使用交叉熵（entropy loss）：
$$
E_t = -y_t \log{\hat {y}_t}
$$

$$
\begin{align}
E(y,\hat y) &= \sum_t E_t(y,\hat y) \notag \\
&= -\sum_t y_t \log \hat y_t
\end{align}
$$

现在用Backpropagation Through Time (BPTT)确定各个权重系数。

一些用到的结论：
$$
\tanh'(x) = 1-\tanh^2(x)
$$
softmax函数的导数$S=softmax(a)$：
$$
\frac{\part S_i}{\part a_j}=
\begin{cases}
S_i(1-S_j), & i=j\\
-S_jS_i, & i\ne j
\end{cases}
$$

### 计算偏导数

首先计算$\frac{\partial E_t}{\partial V}$。因为 $V$ 是矩阵，为帮助理解先按分量计算。为了避免标记混乱这里 $t$ 先不写，各个符号都是 $t$ 时刻的分量（$V$ 除外因为权重共享）。

向量 $\hat y$ 的分量用 $d$ 标记，并定义$z_i=V_{ij}s_j$，然后：
$$
\begin{align}
\frac {\part E}{\part V_{ij}} &=
	\frac{\part E}{\part \hat y}
	\frac{\part \hat y}{\part z_i}
	\frac{\part z_i}{\part V_{ij}}\\
& = \sum_d\frac{\part E}{\part \hat y_d}
	\frac{\part \hat y_d}{\part z_i}s_j\\
& = -y_i(1-\hat y_i)s_j + \sum_{d \ne i} y_d \hat y_is_j\\
& = -y_is_j + \sum_d y_d \hat y_is_j\\
& = (\hat y_i - y_i)s_j
\end{align}
$$
写成向量形式并对 $t$ 求和：
$$
\frac{\part E}{\part V} = \sum_t (\hat y_t -y_t)\otimes s_t
$$
计算 $W$ 和 $U$ 稍微复杂一些，先看 $W$ ：
$$
\begin{align}
\frac {\part E_t}{\part W} &=
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_t}{\part s_{t-1}}
	\frac{\part s_{t-1}}{\part W}\\
\end{align}
$$
因为 $s_t$ 和 $s_{t-1}$ 有关，$s_{t-1}$ 又和 $s_{t-2}$ 有关，一直到 $t=0$ ，根据链式法则：
$$
\begin{align}
\frac {\part E_t}{\part W} &=\sum_{k=1}^{t-1}
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_t}{\part s_{k}}
	\frac{\part s_{k}}{\part W}\\
\end{align}
$$
另外， $\frac{\part s_t}{\part s_k}$ 本身也要用链式法则计算：
$$
\begin{align}
\frac {\part E_t}{\part W} &=\sum_{k=0}^{t-1}
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\left( \prod_{j=k+1}^{t} \frac{\part s_j}{\part s_{j-1}} \right)
	\frac{\part s_{k}}{\part W}\\
\end{align}
$$
公式中的连乘项是梯度消失或梯度爆炸的原因。

计算 $U$ 的方法和 $W$ 差不多：
$$
\begin{align}
\frac {\part E_t}{\part U} &=
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_{t}}{\part U}\\
\end{align}
$$
由于 $x_t$ 和 $s_{t-1}$ 都对 $s_t$ 有贡献，应用链式法则：
$$
\begin{align}
\frac {\part E_t}{\part U} &=
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_{t}}{\part U}
	+
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_t}{\part s_{t-1}}
	\frac{\part s_{t-1}}{\part U}
	+ \cdots\\
	&= \sum_{k=1}^{t}
	\frac{\part E_t}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_t}{\part s_{k}}
	\frac{\part s_{k}}{\part U}
\end{align}
$$
总结一下：
$$
\begin{align}
\frac{\part E}{\part V} &= \sum_t (\hat y_t -y_t)\otimes s_t\\
\frac {\part E}{\part W} &=\sum_t\sum_{k=0}^{t-1}
	\frac{\part E}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\left( \prod_{j=k+1}^{t} \frac{\part s_j}{\part s_{j-1}} \right)
	\frac{\part s_{k}}{\part W}\\
\frac {\part E}{\part U} &= \sum_t\sum_{k=1}^{t}
	\frac{\part E}{\part \hat y_t}
	\frac{\part \hat y_t}{\part s_t}
	\frac{\part s_t}{\part s_{k}}
	\frac{\part s_{k}}{\part U}
	
\end{align}
$$


==怎么样，是不是一下子就懂了？？？==

### Reference:

[1] 图片来源：http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/

[2] arXiv:1610.02583



