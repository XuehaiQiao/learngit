文件开头:

\#!/usr/bin/env python
\# -*- coding: utf-8 -*-

科学记数法， 10用e表示 1.23*10^9 = 1.23e9
print "%d, %f, %s, %x" % (1, 0.1, "string", 13)  -->  integer, flowtingnumber, string, 16进制数

raw_input()	字符串

int()		将字符串改为数字

ctrl+/	批量注释



####list
list = [ ]
len(list)				获得list元素个数
list[number]			列出第number+1个元素（因为从零开始）
list[-number]			从后往前数，-1是最后一个（从一开始）
list.pop(number)		删除第number+1个元素，括号内不填则删除最后一个
list.append("element") 		追加元素至末尾
list.insert(number, "element")	插入元素到指定位置
list[number] = "new element"	替换指定元素
list可以嵌套：
list = [1, [2, 3], 4]
len(list) = 3
list[1] = [2, 3]

####tuple 元组 tuple和list非常类似，但是tuple一旦初始化就不能修改

e.g. tuple = (1, 2, 3)

可以用tuple[number] 来查看

只有一个参数时，tuple = (1,) 要加逗号

tuple更能保证代码安全性，所以最好用tuple在代码中

一种可变tuple

``` python
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
>>> ('a', 'b', ['X', 'Y'])
```



####if

if:

elif:

else:

\>= , \<= , ==

#### for....in....循环

``` python
list = ['Micheal', 'bob', 'Tracy']
for name in list:
  print name
```

结果：

```python
Micheal
Bob
Tracy
```

迭代dict：

迭代value：for value in dict.itervalues():

迭代key和value：for k, v in dict.iteritems():

迭代key：for key in dict:



判断是否为可迭代对象：

方法是通过collections模块的Iterable类型判断：

``` python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的`enumerate`函数可以把一个list变成索引-元素对，这样就可以在`for`循环中同时迭代索引和元素本身：

``` python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print i, value
...
0 A
1 B
2 C
```

上面的`for`循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：

``` python
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print x, y
...
1 1
2 4
3 9
```





#### while 循环

求1-100 奇数和：

``` python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
```



#### dictionary 字典

score = {'Micheal' : 50, 'Bob' : 60, 'Vincent': 100}

dict['key'] = value		一次只能加一个值，不非要是名字和数值，只要对应就行

dict['key']	查字典

检查key是否存在：key in dictionary, 如果是false就是不存在

key必须是不可变对象，例如list就不能当key

dictionary.get('key')

迭代value：for value in dict.itervalues():

迭代key和value：for k, v in dict.iteritems():



#### set： 没有value的dict

a = set([1, 2, 3]) ==>  a = set([1, 2, 3])		set里没有重复

a = set([1, 1, 2, 2, 3]) ==>  a = set([1, 2, 3])

### 函数

函数体内部可以用`return`随时返回函数结果

Python的函数返回多值其实就是返回一个tuple

__默认参数必须指向不变参数__***

e.g. 

```python
def add_end(L = None): #默认参数指向不变参数（list是可变参数）
  	if L is None:
    	L = []
    L.append('end')
	return L

```



#### pass 语句

在函数下加pass 可先跳过该函数，防止报错

####递归：自己引用自己 

 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

#### 切片： 对tuple和字符串一样适用

list[0:10]  =  list[:10]			列出前十个

list[:]	等于list

list[-10:]   =    list[-10:-1]列出后十个

list[::5]		每五个取一个

list[:10:2]	前十个美两个取一个

#### 迭代 iter v. 迭代    iteration n. 迭代

  如果给定一个list或tuple，我们可以通过`for`循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

##列表生成式  list comprehensions 和 列表生成器 list generator

comprehension n. 理解 包含





```python
>>> [x*x for x in range(0,10)] #列表生成式是中括号，储存成list输出
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> (x*x for x in range(0,10)) #列表生成器是小括号，不储存直接输出(不占用内存)
<generator object <genexpr> at 0x7f0b072e6140>

>>> g = (x*x for x in range(0,10))
>>> for n in g:
... 	print n
0
1
4
9
16
25
36
49
64
81
```



range(number, number)

####生成式

e.g.

``` python
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #左闭右开
```

写列表生成式时，把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。这样可以省去循环 (for..in..) 。

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

for循环后面还可以加上if判断 (或在前面加上if, elif, else), 这样我们就可以筛选出仅偶数的平方：

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0] #当只有if时放后面。
[4, 16, 36, 64, 100]

>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() if isinstance(s, str) else s for s in L] #当有if和else等时放前面。
['hello', 'world', 18, 'apple', None]

```



还可以使用两层循环，可以生成全排列：e.g.

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

三层和三层以上的循环就很少用到了。

最后一个把list中所有的字符串变成小写：

```python
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

小结：

运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁

###生成器

```python
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x104feab40>

>>> g = (x * x for x in range(10))
>>> for n in g:
...     print n
...
0
1
4
9
16
25
36
49
64
81
```

将函数返回值从输出变为generator (把 print 换为 yield)

```python
def fib(max):				#普通函数
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

def fib(max):				#generator
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
```

e.g.

```python
>>> def odd():
...     print 'step 1'
...     yield 1
...     print 'step 2'
...     yield 3
...     print 'step 3'
...     yield 5
...
>>> o = odd()
>>> o.next()
step 1
1
>>> o.next()
step 2
3
>>> o.next()
step 3
5
>>> o.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

可以看到，`odd`不是普通函数，而是generator，在执行过程中，遇到`yield`就中断，下次又继续执行。执行3次`yield`后，已经没有`yield`可以执行了，所以，第4次调用`next()`就报错。

回到`fib`的例子，我们在循环过程中不断调用`yield`，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。









