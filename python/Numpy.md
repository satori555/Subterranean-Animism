# Numpy

```python
import numpy as np

a = np.array([[1, 2],
              [3, 4],
              [4, 5]]
            dtype=np.int32)
b = np.ones(6).reshape(2, 3)
np.dot(a, b)
a.dot(b)
np.cumsum(a)
np.diff(a)

# 生成随机数
a = np.random.randint(100, size=30)

# 索引
A = np.arange(3, 15).reshape(3, 4)
print(A[2][1])
print(A[2, 1])
print(A[:, 1])
print(A.flatten())
for item in A.flat:
    print(item)

# 合并
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
np.vstack((A, B))  # [[1 1 1], [2 2 2]]
np.hstack((A, B))  # [1 1 1 2 2 2]

# 分割
np.split(A, 2, axis=1)  # 平均分
np.array_split(A, 3, axis=0)  # 不能平均分
np.vsplit(A, 3)
np.hsplit(A, 2)
```

### 张量转置

```python
import numpy as np

# np.transpose(a,(0, 1, 2)) 或 a.transpose(0, 1, 2)
# 一维向量和二维矩阵的转置很好理解，主要看三维

>>> a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])  # a.shape = (2, 2, 3)
>>> a
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])

>>> b = np.transpose(a,[0,2,1])  # b.shape = (2, 3, 2)
>>> b
array([[[ 1,  4],
        [ 2,  5],
        [ 3,  6]],

       [[ 7, 10],
        [ 8, 11],
        [ 9, 12]]])

>>> b = np.transpose(a,[1,2,0])  # b.shape = (2, 3, 2)
>>> b
array([[[ 1,  7],
        [ 2,  8],
        [ 3,  9]],

       [[ 4, 10],
        [ 5, 11],
        [ 6, 12]]])
```

解释：

考虑列表

```
[[[ 1,  2,  3],
  [ 4,  5,  6]],

 [[ 7,  8,  9],
  [10, 11, 12]]]
```

第0个轴(axis=0)方向为：1 -> 7

第1个轴(axis=1)方向为：1 -> 4

第2个轴(axis=2)方向为：1 -> 2



对于初始的（0,1,2）格式，列表里的元素按（axis=2->axis=1->axis=0）的顺序输出，也就是原本的顺序和shape。

转置为（0,2,1）格式，按（1,2,0）顺序，先输出1,4，然后0方向没有了（加一层方括号），2方向是2,5，然后是3,6（这里1方向也没有了，再加一层方括号）等等：

    [[[ 1,  4],
      [ 2,  5],
      [ 3,  6]],
    
     [[ 7, 10],
      [ 8, 11],
      [ 9, 12]]]
转置为（1,2,0）格式，按（0,2,1）顺序，先1,7，然后2,8等等：

```
[[[ 1,  7],
  [ 2,  8],
  [ 3,  9]],

 [[ 4, 10],
  [ 5, 11],
  [ 6, 12]]]
```

也可以放到三维坐标图里帮助理解，参考： https://www.cnblogs.com/xiaoboge/p/9682364.html 



