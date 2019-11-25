# Gated Recurrent Unit (GRU)

GRU的网络结构如图：

 ![img](D:\Users\test\Documents\GitHub\Subterranean-Animism\image_storage\20170814103515255.png) 

GRU是LSTM的一个变体，只有两个门：更新门$z_t$和重置门$r_t$。

公式：
$$
r_t=\sigma(W_r\cdot[h_{t-1},x_t]) \\
z_t=\sigma(W_z\cdot[h_{t-1},x_t]) \\
\tilde h_t=\tanh(W_{\tilde h}\cdot[r_t*h_{t-1},x_t]) \\
h_t=(1-z_t)*h_{t-1}+z_t*\tilde h_t \\
y_t=\sigma(w_o\cdot h_t)
$$
其中[]表示两个向量连接，*表示矩阵元素相乘。



### 参考资料：

[1] https://blog.csdn.net/wangyangzhizhou/article/details/77332582