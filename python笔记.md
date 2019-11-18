[TOC]

## 1. 字符串

str.join(seq)：序列seq的所有元素以字符str连接

s.split(str=' ', num)：str分隔符，默认空字符（空格 \n \t等），num分割次数

s.strip()：删除字符串头尾指定字符，默认为空格或换行符

格式化字符串

```python
>>>str = "the length of (%s) is %d" %('runoob',len('runoob'))
```

字符串前面的 r b u f

r：去除转义字符，常用于正则表达式

f：表示字符串内支持大括号内的python表达式

b：表示后面字符串是bytes类型。网络编程中，服务器和浏览器只认bytes类型数据

u：后面的字符串以Unicode格式编码，一般用于中文字符串前面

## 2. 列表

list.append()：向列表尾部添加一个新元素

list.extend()：只接受一个列表作为参数，添加到原有列表中

list = [0 for _ in range(100)]



## 3. 字典

dict2 = dict1.copy()：浅拷贝

dict.update(dict2)
把字典dict2的键/值对更新到dict里，可用于合并

dict1 = dict.fromkeys(seq[, value])

创建一个新字典，以列表 seq 中元素做字典的键，value 为所有键的初始值

dict.get(key, default=None)

返回指定键的值，如果值不在字典中返回default值。

dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default

dict.has_key(key)
如果键在字典dict里返回true，否则返回false

dict.items()
以列表返回可遍历的(键, 值) 元组数组

dict.keys()，dict.values()
以列表返回一个字典所有的键，值



## 4. 文件

读文件

```python
with open(file, 'r', encoding='utf-8') as fp:
    for line in fp.readlines():
        pass
```

写文件

```python
with open(w_file, 'w', encoding='utf-8') as wp:
    wp.write(content)
```



## 5. 输入输出

输入input()，可以接收python表达式

```python
>>>str = input("请输入：")
请输入：[x*5 for x in range(2,10,2)]
```

格式化输出

```python
>>>str = "the length of (%s) is %d" %('runoob',len('runoob')) 
>>>print(str)
the length of (runoob) is 6 
```

str.format()

```python
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
 
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
```



## 6. 异常

实例：

```python
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
```

try-except

```python
try:
    正常的操作
except(Exception1[, Exception2[,...ExceptionN]]):
   发生以上多个异常中的一个，执行这块代码
else:
    如果没有异常执行这块代码
```

try-finally

```python
try:
    <语句>
finally:
    <语句>    #退出try时总会执行
raise
```

raise：自己触发异常

```python
raise [Exception [, args [, traceback]]]
```

常用异常

| 错误类型          | 说明                                                         |
| ----------------- | ------------------------------------------------------------ |
| AttributeError    | 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x      |
| IOError           | 输入/输出异常；基本上是无法打开文件                          |
| ImportError       | 无法引入模块或包；基本上是路径问题或名称错误                 |
| IndentationError  | 语法错误（的子类）；代码没有正确对齐                         |
| IndexError        | 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]    |
| KeyError          | 试图访问字典里不存在的键                                     |
| KeyboardInterrupt | Ctrl+C被按下                                                 |
| NameError         | 使用一个还未被赋予对象的变量                                 |
| TypeError         | 传入对象类型与要求的不符合                                   |
| ValueError        | 传入一个调用者不期望的值，即使值的类型是正确的               |
| UnboundLocalError | 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它 |



## 7. 正则表达式

在线测试工具： http://c.runoob.com/front-end/854 



| 元字符 | 匹配内容                                                     |
| ------ | ------------------------------------------------------------ |
| .      | 匹配除换行符以外的任意字符                                   |
| \      | 将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。 |
| \w \W  | 匹配（非）字母或数字或下划线                                 |
| \s \S  | 匹配任意的（非）空白符                                       |
| \d \D  | 匹配（非）数字                                               |
| \n \t  | 匹配一个换行符（制表符）                                     |
| \b     | 匹配一个单词的结尾                                           |
| ^ $    | 匹配字符串的开始（结尾）                                     |
| a\|b   | 匹配字符a或字符b                                             |
| ()     | 匹配括号内的表达式，也表示一个组                             |
| [...]  | 匹配字符组中的字符                                           |
| [^...] | 匹配除了字符组中字符的所有字符                               |

| 量词  | 说明                         |
| ----- | ---------------------------- |
| *     | 重复零次或更多次，等价于{0,} |
| +     | 重复一次或更多次，等价于{1,} |
| ?     | 重复零次或一次（非贪婪匹配） |
| {n}   | 重复n次                      |
| {n,}  | 重复n次或更多次              |
| {n,m} | 重复n到m次                   |

| 常见组合 | 说明                                |
| -------- | ----------------------------------- |
| .*?x     | 取前面任意长度的字符，直到一个x出现 |
|          |                                     |
|          |                                     |

python re 模块

```python
import re

ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
print(ret) #结果 : ['a', 'a']

ret = re.search('a', 'eva egon yuan')
if ret:
	print(ret.group()) #结果 : 'a'
# re.search函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串。如果字符串没有匹配，则返回None，此时调用group()会报错。

ret = re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
print(ret)
#结果 : 'a'

ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

ret = re.split('([ab])', 'abcd')  # 匹配部分加()保留匹配的项
print(ret)  # ['', 'a', '', 'b', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

import re
ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果
```

举例：

```python
# 匹配新闻中的关键词
# 过滤 记者 | xx
s = re.search(r'[\|｜].+?\s', string)
if s:
    return string.split(s.group())[-1]
# 过滤 新京报讯（记者 xxx）...
s = re.search(r'[(（]记者.*?[）)]', string):
if s:
    return string.split(s.group())[-1]
```



## 8. 赋值

直接赋值、浅拷贝和深度拷贝

```python
import copy
b = a
# 直接赋值是一个完完全全的引用，对新变量的任何改动都会影响到原对象。
c = copy.copy(a)
# 浅拷贝创建了新的对象，但是只拷贝了序列的元素，对于元素也是一个序列的情况（即子对象），只复制了对这个序列的引用！如 a[0] = [1, 2] 是一个列表，则相当于 c[0] = a[0]。
d = copy.deepcopy(a)
# 深拷贝是完完全全的拷贝，把原对象完整地拷贝到了新对象中。对新变量的改动不影响原变量。
```

## 9. 函数

```python
lambda x, y : (x + y) 
```

lambda表达式。冒号左边是参数，用逗号隔开，冒号右边是返回值。

```python
filter(function, iterable)
```

接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

```python
map(function, iterable, ...)

>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
```

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

装饰器

```python
def a(func):
    def b():
        print('洒点水')
        func()
    return b

@a  # 装饰器语法糖
def create_people():
    print('女娲真厉害，捏个泥吹口气就成了人！')

create_people()
# 洒点水
# 女娲真厉害，捏个泥吹口气就成了人！
```

函数的链式调用：

```python
# python 函数的链式调用
def funcA(a):
    def funcB(b):
        for a_each in a:
            x = funcB(a_each)
        return x
    return funcB

print(funcA(3)(5))
 
# 等价于
func = funcA(3)
print(func(5))
```



## 10. 面向对象

继承，封装，多态