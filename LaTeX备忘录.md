# LaTeX备忘录

持续更新，想到什么加什么。

### 上下标和运算符

向量：$\vec x$ 加粗：$\boldsymbol x$

字母上的特殊符号：$\widetilde P$ $\hat x$  $\dot x$ $\ddot x$ $\overline x$ 

将下标放在正下方 $\max \limits_x f(x)$  
$$
\mathop{\arg\max}_\theta
$$
圆圈 $a\circ b$  加减 $\pm$ 乘号 $\times$  除号 $\div$  直积 $\otimes$ 元素相乘 $\odot$ 点乘 $a\cdot b$ 横点 $\dots$ 竖点 $\vdots$  

各种等号 $\equiv \simeq \doteq \approx \propto \neq$  不等号 $\le \ge \ll \gg$

波浪号 $\sim$ 箭头 $\to$ 属于 $\in$ 交集 $\cap$ 并集  $\cup$ 无穷大 $\infty$ 

左右箭头 $\leftrightarrow$ $\Leftrightarrow$

求和$\sum$ 连乘 $\prod$ 



### 大型公式

多行公式对齐
$$
\begin{align}
f(x) &= x1 \\
&= x2 \notag \\
&= x3
\end{align}
$$

$$
f(x)=
\begin{cases}
\cos(t) & t=1 \\
\sin(t) & t\ne 1
\end{cases}
$$

$$
\begin{Bmatrix}
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9
  \end{Bmatrix} \tag{M}
$$
行间矩阵：我们使用矩阵 $\bigl( \begin{smallmatrix} a & b \\ c & d \end{smallmatrix} \bigr)$ 作为因子矩阵，将其...



用\left和\right来显示不同的括号：

小括号：$\left( \frac 12 \right)$ 花括号：$\left\{ \frac 12 \right\}$ 绝对值：$\left| x \right|$ $\left\| x \right\|$





### 空格

| 不同长度的空格 |            |             |                |
| -------------- | ---------- | ----------- | -------------- |
| 两个quad空格   | a \qquad b | $a\qquad b$ | 两个*m*的宽度  |
| quad空格       | a \quad b  | $a \quad b$ | 一个*m*的宽度  |
| 大空格         | a\ b       | $a\ b$      | 1/3*m*宽度     |
| 中等空格       | a\;b       | $a\;b$      | 2/7*m*宽度     |
| 小空格         | a\,b       | $a\,b$      | 1/6*m*宽度     |
| 没有空格       | ab         | $ab$        |                |
| 紧贴           | a\\!b      | $a\!b$      | 缩进1/6*m*宽度 |



### 希腊字母

| 希腊字母                            |                               |                         |                         |
| ----------------------------------- | ----------------------------- | ----------------------- | ----------------------- |
| $\alpha$ $\Alpha$                   | $\eta$ $\Eta$                 | $\nu$ $\Nu$             | $\tau$ $\Tau$           |
| $\beta$ $\Beta$                     | $\theta$ $\vartheta$ $\Theta$ | $\xi$ $\Xi$             | $\upsilon$ $\Upsilon$   |
| $\gamma$ $\Gamma$                   | $\iota$ $\Iota$               | $\omicron$ $\Omicron$   | $\phi$ $\varphi$ $\Phi$ |
| $\delta$ $\Delta$                   | $\kappa$ $\Kappa$             | $\pi$ $\Pi$             | $\chi$ $\Chi$           |
| $\epsilon$ $\varepsilon$ $\Epsilon$ | $\lambda$ $\Lambda$           | $\rho$ $\varrho$ $\Rho$ | $\psi$ $\Psi$           |
| $\zeta$ $Zeta$                      | $\mu$ $\Mu$                   | $\sigma$ $\Sigma$       | $\omega$ $\Omega$       |


