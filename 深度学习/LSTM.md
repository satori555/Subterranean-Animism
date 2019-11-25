---
typora-root-url: ..\image_storage
---

# Long short-term memory (LSTM)

LSTM可以解决普通RNN的梯度消失问题。

回忆一下普通RNN，当前时刻的输出$z_t$取决于隐藏层$h_t$，而隐藏层$h_t$取决于当前时刻的输入$x_t$和上一时刻的隐藏层$h_{t-1}$。LSTM在RNN的基础上，多了一个隐藏状态$C_t$和四个门控结构，如图：

![image-20191125221852777](D:\Users\test\Documents\GitHub\Subterranean-Animism\image_storage\image-20191125221852777.png)

四个门分别接收当前时刻的输入$x_t$和上一时刻隐藏层的状态$h_{t-1}$，然后计算隐藏状态$C_t$，最后隐藏状态$C_t$和输出门$o_t$决定当前时刻的隐藏层$h_t$，同时输出$z_t$。公式如下：
$$
f_t=\sigma(W_{xf}x_t+W_{hf}h_{t-1}+b_f) \\
i_t=\sigma(W_{xi}x_t+W_{hi}h_{t-1}+b_i) \\
g_t=\tanh(W_{xc}x_t+W_{hc}h_{t-1}+b_c) \\
c_t=f_t\circ c_{t-1}+i_t\circ g_t \\
o_t=\sigma(W_{xo}x_t+W_{ho}h_{t-1}+b_o) \\
h_t=o_t\circ\tanh(c_t) \\
z_t=softmax(W_{hz}+b_z)
$$
误差逆传播的推导以后再补充。

 

## 参考资料：

[1] arXiv:1610.02583

[2] http://colah.github.io/posts/2015-08-Understanding-LSTMs/

[3] https://blog.csdn.net/zhangbaoanhadoop/article/details/81952284