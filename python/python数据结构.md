# python数据结构

### 栈和队列

栈和队列都可以用列表实现。Python的collections模块里有一个双向队列deque。

```python
from collections import deque
```



### 链表

```python
class Node:  
    def __init__(self, data):
        self.data = data  
        self.next = None 
```



### 二叉树

```python
class Node(object):
    def __init__(self,item):
        self.item=item #表示对应的元素
        self.left=None #表示左节点
        self.right=None #表示右节点
    def __str__(self):
        return str(self.item)  #print 一个 Node 类时会打印 __str__ 的返回值
```



### 字典树

```python
class TrieNode:
    def __init__(self):
        self.nodes = dict()  # 构建字典
        self.is_leaf = False
    def insert(self, word: str):  
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True
    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)
    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf
```



### 堆

```python
class heap(object):
    def __init__(self):
        #初始化一个空堆，使用数组来在存放堆元素，节省存储
        self.data_list = []
    def get_parent_index(self,index):
        #返回父节点的下标
        if index == 0 or index > len(self.data_list) -1:
            return None
        else:
            return (index -1) >> 1
    def swap(self,index_a,index_b):
        #交换数组中的两个元素
        self.data_list[index_a],self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]
    def insert(self,data):
        #先把元素放在最后，然后从后往前依次堆化
        #这里以大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        self.data_list.append(data)
        index = len(self.data_list) -1 
        parent = self.get_parent_index(index)
        #循环，直到该元素成为堆顶，或小于父节点（对于大顶堆) 
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            #交换操作
            self.swap(parent,index)
            index = parent
            parent = self.get_parent_index(parent)
    def removeMax(self):
        #删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        #堆化
        self.heapify(0)
        return remove_data
    def heapify(self,index):
        #从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) -1
        while True:
            maxvalue_index = index
            if 2*index +1 <=  total_index and self.data_list[2*index +1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index +1
            if 2*index +2 <=  total_index and self.data_list[2*index +2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index +2
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)
            index = maxvalue_index
```



参考：

[1] 常见数据结构的 Python 实现（建议收藏） - 知乎
https://zhuanlan.zhihu.com/p/78785861