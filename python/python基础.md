# Python基础

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



## 6. 读写Excel文件

```python
import xlrd
import xlwt

# 基础操作 #

# 读取Excel文件
excel = xlrd.open_workbook('test.xlsx')
sheet = excel.sheet_by_name('Sheet1')  # 通过名字获取表格
sheet = excel.sheet_by_index(0)  # 通过索引获取表格
rows = sheet1.row_values(2)  # 获取行内容
cols = sheet1.col_values(3)  # 获取列内容
for rid in range(sheet.nrows):
    label = sheet.cell_value(row, col)
    label = sheet.cell(row, col).value

# 写入Excel文件
workbook = xlwt.Workbook(encoding='utf-8')  # 注意Workbook大写
worksheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
worksheet.write(row, col, content)
workbook.save('test.xlsx')

```

Python读取Excel中单元格的内容，返回的有5种类型：

ctype :  0 empty，1 string，2 number， 3 date，4 boolean，5 error

注意number默认为float类型。

读取日期：xlrd.xldate_as_tuple()

```python
import xlrd
from datetime import date,datetime

print(sheet1.cell(1,2).ctype)
if sheet1.cell(1, 2).ctype == 3:  # date类型
	date_value = xlrd.xldate_as_tuple(sheet1.cell_value(1,2),wb.datemode)
print(date_value)
print(date(*date_value[:3]))
print(date(*date_value[:3]).strftime('%Y/%m/%d'))
```



使用Pandas处理Excel [1]

```python
import pandas as pd

df=pd.read_excel('lemon.xlsx',sheet_name='student')  # 不指定sheet_name默认读取第一个表单
data=df.head()  # 默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data))#格式化输出
```



Reference:

[1] Python利用pandas处理Excel数据的应用 - 华妹陀 - 博客园
https://www.cnblogs.com/liulinghua90/p/9935642.html