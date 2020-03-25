# python深浅拷贝问题
# Python中，对象的赋值，拷贝（深/浅拷贝）之间是有差异的，如果使用的时候不注意，就可能产生意外的结果。
#
# 下面本文就通过简单的例子介绍一下这些概念之间的差别。
#
# 一、对象赋值
# 　　又叫变量对对象的引用

# li=["Will", 28, ["Python", "C#", "JavaScript"]]
# new_li=li

# print(id(li)) #1369658120136
# print([id(ele) for ele in li]) #[1369692104328, 1511377424, 1369692110600]
#
# print(id(new_li)) #1369658120136
# print([id(ele) for ele in new_li]) #[1369692104328, 1511377424, 1369692110600]

'''
li赋值给了new_li，同时，new_li是引用了li的内存地址

　　当对数据做修改的操作时：

　　1、经本人多次试验考证，发现对象赋值，不论多么复杂的数据结构，你对任意数据做了修改之后，都会影响到另一个

　　2、而且，若数据为可变数据类型，修改数据后，内存地址都不会变

　　3、若为不可变数据类型，修改数据后，会替换掉旧的对象，即内存地址会发生改变　
'''


# li=["Will", 28, ["Python", "C#", "JavaScript"]]
# new_li=li
#
# print([id(ele) for ele in li]) #[1925751432840, 1511377424, 1925751446472]
#
# li[0] = "Wilber"
# li[1] = 22
# li[2].append("CSS")
#
# print ([id(ele) for ele in li]) #[1925751447768, 1511377232, 1925751446472]


#二、浅拷贝

# import copy
# li=["Will", 28, ["Python", "C#", "JavaScript",[
#     {'mm':1},
#     {'mm':2},
#     {1,2,3}
# ]]]
#
# new_li=copy.copy(li)
#
# print([id(ele) for ele in li]) #[1474180867888, 1511377424, 1474180874120]
# print([id(ele) for ele in new_li]) #[1474180867888, 1511377424, 1474180874120]
#
# new_li[0] = "Wilber"
# new_li[1] = 22
# new_li[2].append("CSS")
# new_li[2][3][0]='xx'
# new_li.append('sss')
#
# print (li) #['Will', 28, ['Python', 'C#', 'JavaScript', ['xx', {'mm': 2}, {1, 2, 3}], 'CSS']]
# print ([id(ele) for ele in li]) #[1474180867888, 1511377424, 1474180874120]
#
# print (new_li) #['Wilber', 22, ['Python', 'C#', 'JavaScript', ['xx', {'mm': 2}, {1, 2, 3}], 'CSS'], 'sss']
# print ([id(ele) for ele in new_li]) #[1474180883040, 1511377232, 1474180874120]

# 浅拷贝只拷贝了最外面一层的数据，当对最外面一层做改动时，不会影响到另一个，但是对套在里面的数据做改动就会影响到另外一个。
# 　　注：切片的效果和浅拷贝一样


# 三、深拷贝
#深拷贝对每一层数据都做了拷贝，即对任一数据做了改动，都不会影响到另一个

# import copy
# li=["Will", 28, ["Python", "C#", "JavaScript",[
#     {'mm':1},
#     {'mm':2},
#     {1,2,3}
# ]]]
# new_li=copy.deepcopy(li)
#
# print([id(ele) for ele in li]) #[1609895241352, 1511377424, 1609895247752]
# print([id(ele) for ele in new_li]) #1609895241352, 1511377424, 1609895247816]
#
# new_li[0] = "Wilber"
# new_li[1] = 22
# new_li[2].append("CSS")
# new_li[2][3][0]='xx'
# new_li.append('sss')
#
# print (li) #['Will', 22, ['Python', 'C#', 'JavaScript', [{'mm': 1}, {'mm': 2}, {1, 2, 3}]]]
# print ([id(ele) for ele in li]) #[1609895241352, 1511377232, 1609895247752]
#
# print (new_li) #['Wilber', 28, ['Python', 'C#', 'JavaScript', ['xx', {'mm': 2}, {1, 2, 3}], 'CSS'], 'sss']
# print ([id(ele) for ele in new_li]) #[1609895256448, 1511377424, 1609895247816, 1609895256728]
#
# '''
# 四、总结
# 　　1、对象赋值是对对象内存地址的引用，它代表原始对象，所以不论对哪一个做了改动，都会影响到另外一个
#
# 　　2、copy.copy()浅拷贝，只对第一层元素进行拷贝
#
# 　　3、若想复制一个容器对象及里面的所有元素（包含元素的子元素），可以使用copy.deepcopy()进行深拷贝
#
# 　　4、对于非容器类型（如数字、字符串、等不可变类型的对象）没有被拷贝一说
# '''




