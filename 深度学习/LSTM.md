# Long short-term memory (LSTM)

LSTM可以解决普通RNN的梯度消失问题，可以学习长期依赖信息。

回忆一下普通RNN，当前时刻的输出$z_t$取决于隐藏层$h_t$，而隐藏层$h_t$取决于当前时刻的输入$x_t$和上一时刻的隐藏层$h_{t-1}$。LSTM在RNN的基础上，多了两个Cell状态$C_t,\widetilde C_t$和三个门控结构$i_t,f_t,o_t$，如图：

![lstm](..\image_storage\LSTM3-chain.png)

先看公式：
$$
\begin{align}
f_t=\sigma(W_{xf}x_t+W_{hf}h_{t-1}+b_f) \\
i_t=\sigma(W_{xi}x_t+W_{hi}h_{t-1}+b_i) \\
\widetilde C_t=\tanh(W_{xc}x_t+W_{hc}h_{t-1}+b_c) \\
o_t=\sigma(W_{xo}x_t+W_{ho}h_{t-1}+b_o) \\
C_t=f_t\circ C_{t-1}+i_t\circ \widetilde C_t \\
h_t=o_t\circ\tanh(C_t) \\
z_t=softmax(W_{hz}h_t+b_z)
\end{align}
$$
矩阵形式：
$$
\left [ \begin{matrix}
f_t \\ i_t \\ \widetilde C_t \\ o_t
\end{matrix} \right ]
=
\left [ \begin{matrix}
\sigma \\ \sigma \\ \tanh \\ \sigma
\end{matrix} \right ]
\left( W^T
\left [ \begin{matrix}
x_t \\ h_{t-1}
\end{matrix} \right ]
+b \right)
$$

### 如何理解LSTM？

普通的RNN中，$h_{t-1}$只能保存短时记忆，LSTM通过Cell状态可以保存长期的记忆。

三个门经过sigmoid函数被映射到0到1之间，做乘法后可以控制记忆（1）或遗忘（0）。公式（5，6）中圆圈代表矩阵中对应元素相乘。

公式（3）生成一个备选状态$\widetilde C_t$，公式（5）的第一项参数控制上一时刻Cell状态$C_{t-1}$哪些要留下哪些要遗忘，第二项参数控制新加入的Cell状态，然后得到当前cell状态$C_t$。

当前的隐藏层状态$h_t$由Cell状态和输入门$o_t$一起决定。

最后由$h_t$输出$z_t$。



### BiLSTM

LSTM的一个变种，输入数据通过前向与后向的LSTM，然后拼接。

### LSTM参数数量

设输入层有1000个cell，LSTM有2000个cell，则参数数量为$(1000\times2000\times2+2000)\times4\approx16M$



### 参考资料：

[1] arXiv:1610.02583

[2] http://colah.github.io/posts/2015-08-Understanding-LSTMs/

[3] https://zhuanlan.zhihu.com/p/27118363