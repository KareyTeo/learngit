#tip:定义默认参数要牢记一点：默认参数必须指向不变对象！




# -*- coding: utf-8 -*-

#======================
#默认参数
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L




#======================
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax ^ 2 + bx + c = 0
# ax2+bx + c = 0的两个解。
# 计算平方根可以调用math.sqrt()函数

# import math
#
# def quadratic(a, b, c):
#     d = float(b ** 2 - 4 * a * c)
#
#     if a == 0:
#         return -c/b
#
#     if d < 0:
#         return 'none'
#     else:
#         s = math.sqrt(d)
#         x1 = ((-b + s) / (2 * a))  # 英文符号，出过错
#         x2 = ((-b - s) / (2 * a))
#         return x1, x2
#
#
# # (2*a)，否则运算顺序出错
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 0, 4) =', quadratic(1, 0, 4))
# print('quadratic(0, 1, 4) =', quadratic(0, 1, 4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 0, 4) != 'none':
#     print('测试失败')
# elif quadratic(0, 1, 4) != - 4.0:  # 一开始忘加引号
#     print('测试失败')
# else:
#     print('测试成功')

#input()  # wait




#======================
#汉诺塔，请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
#     if n == 1:
#         print('move', a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1, a, b, c)
#         move(n-1, b, a, c)
#
# move(4, 'A', 'B', 'C')




#======================
# print('for x in iter([1, 2, 3, 4, 5]):')
# for x in iter([1, 2, 3, 4, 5]):
#     print(x)



#======================
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L = [x.lower() if isinstance(x,str) else x for x in L1]
# print(L)


#======================
# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
# 注意，赋值语句：
# a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(5)

#======================
#闭包
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()


#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())




#======================
#利用闭包返回一个计数器函数，每次调用它返回递增整数
# def createCounter():
#   n = 0               # 先定义一个变量作为初始值
#   def counter():      # 定义一个内部函数用来计数
#     nonlocal n        # 声明变量n非内部函数的局部变量，否则内部函数只能引用，一旦修改会视其为局部变量，报错“局部变量在赋值之前被引用”。
#     n += 1            # 每调用一次内部函数，对n + 1
#     return n          # 返回n的值
#   return counter
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')



#======================
# l=list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l)
#
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
# print(L)
#
#
# #======================
# #简单装饰器
#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# 由于now 指向log(now).
#
# 而log 返回的是wrapper函数.
#
# wrapper函数首先print，然后调用了 func,即代码中的func(```)
#
# 对于第二种

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# now = log('string')(now)

# log('string')返回的是decorater函数.
#
# 相当于decorater(now)且text='string'




#======================
#格式化字符串format

# a = 'hello'
# b = 'world'
# p = ['abc',18]
# l = ['asd','qwe']
# #不指定位置
# print('{}:{}'.format('hello','world'))
# print('{}:{}'.format(a, b))
#
# #位置参数，指定位置
# print('{1}:{0}'.format(a,b))
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
#
# #关键字参数,需要在format后关键字后输入值
# print('输入{a}，输入{b}' .format(a='aaa',b='bbb'))
#
# #下标
# print('下标{0[0]},下标{1[1]}'.format(p,l))
#
# #python3.5以上，f 格式化
# print(f'f格式化{a}')



#======================
# math模块的使用
# ceil：取大于等于x的最小的整数值，如果x是一个整数，则返回x本身。
# fbs：用于取绝对值，返回的是一个浮点数。
# floor：取小于或等于x的最大的整数值，如果x是一个整数，则返回x本身。
# fsum：主要用作于列表或其他迭代器类型的变量，对里面的每个元素求和，返回的是浮点数。
# pow：幂运算。
# sqrt：对x进行开方操作
# import math
# print(math.fabs(-5))
# print(math.ceil(3.4))
# print(math.ceil(3))
# print(math.ceil(3.6))
# print(math.floor(2.3))
# print(math.floor(-2.4))
# print(math.fsum([1,2,3]))
# print(math.pow(2,3))
# s=math.sqrt(5)
# print('%.2f' % s)
# print('{:.3f}'.format(s))


#======================
# random模块的使用
# random.random()：返回[0.0, 1.0)之间的浮点数。注意：这个是左闭右开的区间，能取到0.0，但无法取到1.0。
#
# random.randint(a,b): 生成一个a与b之间的随机整数，[a,b]
#
# random.randrange(a, b): 生成一个a与b之间的随机整数，[a,b)
#
# random.uniform(a, b)：生成[a,b]随机的浮点数
#
# random.choic([]): 从列表中随机选择一个数。
#
# random.shuffle([]): 打乱列表中元素的顺序。
#
# random.sample([], n): 从列表中随机取出n个元素

# import random
# print(random.random())
# print(random.randint(2,10))
# print(random.randrange(2,10))
# print(random.uniform(2,10))
# print(random.choice([2,3,11]))
#
# print(random.shuffle([2,3,5]))
# a=[1,2,3]
# random.shuffle(a)
# print(a)
#
# b=random.sample([1,2,3],2)
# print(random.sample([1,2,3],2))
# print(b)




#======================
# print('hello'.islower())
# print('Hello'.islower())
# print('Hello'.upper())
#
# # strip：删除原字符串中左右两边指定的字符，如果不指定删除的字符，则默认删除左右两边的空白字符
# s = '   ####欢迎大家来到蜗牛学院######学习python课程,预祝大家学习顺利####'
# print(s.strip())
# # lstrip,rstrip: 删除原字符串中左边(lstrip)或右边(rstrip)指定的字符
# print(s.strip('#'))
#
# #swapcase反转大小写
#
# print(s.rstrip('#'))
# s1='hello world '
# s2 = ['a','b']
# print(s1.title())
# print(s1.capitalize())
# print(s1.swapcase())
# print(list(s1))
# print(tuple(s1))
# print(s1.expandtabs(8))
# print(s1.split(' '))
# print(s1.partition(' '))
# print(s1.join(s2))
# print(isinstance(s1,str))
# print(type(s1))
# print(dir(s1))
# print(str(s1))
# print(repr(s1))


# q=[3,5,9,6,8,0]
# # 从大到小排列
# # q.sort(reverse=True)
# q.sort()
# print(q)


#列表含有字符串排序
# q1 =[2,4,5,'0','1']
# q1.sort(key=lambda x: int(x))
# print(q1)

# import copy
# a=[1,2,5,4,8]
# b=a[:]
# c=copy.copy(a)
# d=copy.deepcopy(a)
# e = list(range(0,5))
# f = [ i if i % 2 ==0 else -i for i in e ]
# a.append(7)
# print(a)
# print(b)
# print(c)
# print(d)
# print(min(a))
# print(e)
# print(f)

print(__name__)
