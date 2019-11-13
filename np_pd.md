## numpy

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





## pandas





