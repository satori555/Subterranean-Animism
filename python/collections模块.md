# collections

### defaultdict

```python
# defaultdict，当key不存在时返回默认值
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict5 = defaultdict(lambda: 'N/A')

print(dict1[1])  # 0
print(dict2[1])  # set()
print(dict3[1])  # 
print(dict4[1])  # []
print(dict5[1])  # N/A 
```

### deque

```python
# deque，双端队列
from collections import deque

d = deque(['a', 'b'])
d.append('c'）
d.pop()
d.appendleft('z')
d.popleft()
# 还有extend，insert等方法
# 可以指定队列长度，超出长度从左边弹出
d = deque(range(10), maxlen=10)
print(d)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
d.extend('abc')
print(d)  # deque([3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c'], maxlen=10)
```

### namedtuple

```python
# namedtuple，给元组中的元素取名字，类似字典
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'age', 'type'])
perry = Animal(name="perry", age=31, type="cat")
print(perry.name)  # perry
```

### Counter

```python
# Counter，计数器，是字典的字类
# 返回一个以元素为key、元素个数为value的Counter对象集合
from collections import Counter

c = Counter('programming')
print(c)
# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
```

