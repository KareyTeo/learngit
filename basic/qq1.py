# while 1:
#     i = input("请输入：")
#     print(type(eval(i)))
#     if i == "quit":
#         break
# else:
#     print('结束')

# def test(*para):
#     print('有 %d 个参数' % len(para))
#     return para
#
# a = [1,2,3,4]
#
# print(test(*a))
# print('-----')
# print(test(1,2,3,45,8))

# class  student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.study()
#         #私有类属性
#         self.__do_thing()
#     def study(self):
#         print(self.age)
#         self.sleep()
#     def sleep(self):
#         print("%s正在睡觉" % self.name)
#         #self.__do_thing()
#     def __do_thing(self):
#         """
#         私有方法
#         """
#         print('私有方法')
#     def aaa(self):
#         print('无self调用')
#     def __del__(self):
#         pass
#     @staticmethod
#     def eat():
#         print('静态')


#使用@staticmethod类名调用静态方法student.eat()

#对象调用静态方法
# student('zkl',22,'feamle').eat()
#s = student('zhf',22,'m')
#s.eat()



"""
以追加的方式打开文件，每写入一行就读取一行并打印出来
"""
import os
from datetime import datetime
# import time
#
# while True:
#     time.sleep(2)
#     f = open('/Users/karey/test/test.txt', 'a+')
#     #写数据之前的位置
#     pos = f.tell()
#     print(pos)
#     f.write('\nthis time :' + datetime.now().strftime('%H:%M:%S') + '\n')
#     #写数据之后的位置
#     new_pos =f.tell()
#     #移动到之前的位置
#     f.seek(pos,0)
#     #读取数据
#     line = f.read()
#     print(line)
#     #读完后，移动到写数据之后的位置
#     f.seek(new_pos)
#     #print('pos: %d, new_pos: %d\n'% (pos, new_pos))


# #定义变量x，连续赋值3次并打印
# n = 1
# while n < 4:
#     x = input("请输入x的值:")
#     print(x)
#     n = n +1

#创建字典，访问字典
# a = {}.fromkeys(['a', 'b', 'c'])
# b = {'a':1, 'b':2,'c':3 }
# print(a,b)
# print(a['a'])

#计算200以内质数
#什么是质数，除以1和自身以外，没有可以被整除因子
#如何判断整除：n % i == 0，表明可以整除。或判断n / i 是否与 n // i 相等
#如何来整除1到自身的所有数？循环1到自身，并逐个尝试。200以内就从1到200循环，对每一个数字即可

l = []
loop = 0
for n in range(1,200):
    for i in range(2,int(n/2)+1):
        loop += 1
        if n % i == 0:
            break
    else:
        l.append(n)
print(l)
print(len(l))
print("本次循环次数是：%d " % loop)


#69进制转换，图片是二进制文件


#70函数：可复用可模块化

#对输入的字符串进行判断，确认其是否可以转换为一个有效的数字
def check_number(string):
    negative = 0
    point = 0
    is_valid = True
    for c in string:
        code = ord(c)
        if (code < 48 and code != 46) or code >57:
            is_valid =False
            break
        elif code ==45:negative += 1
        elif code ==46:point += 1

    if negative > 1: is_valid = False
    if point > 1: is_valid = False
    if negative == 1 and string[0] != '-': is_valid = False

    return is_valid

















