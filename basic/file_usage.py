#文件操作，读写 input/output

#open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)

"""
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first，只能写，覆盖整个文件，不存在则创建
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists 只能写，从文件底部添加内容，不存在则创建
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
'r+'      可读可写，不会创建不存在的文件，从顶部开始写，会覆盖之前此位置的内容              ----不会创建不存在文件，一般不使用
'w+'      可读可写，如果文件存在，则覆盖整个文件，不存在则创建                           ----覆盖原有文件
'a+'      可读可写，从文件顶部读取内容，从文件底部添加内容 不存在则创建                   ----追加内容
========= ===============================================================
"""


def read_text():
    file = open('/Users/karey/PycharmProjects/new1/test.txt')
    line_list = file.readlines()                                                  #将文件的按行读取到一个列表
    print(line_list)  # print自带换行，不需要换行的话参数end=''
    for line in line_list:
        print(line,end = '')

    for i in range(3):
        print(file.readline())   #一行一行读，输出一行
        print(file.readline())   #输出下一行
        print(file.readline())   #输出下下一行
        print(file.readline(6))   #读出一行的 六个字符

    content = file.read()                                                          #读取整个内容，并以字符串返回
    print(type(content))
    print(file.read(10))  #读出10字符

    print(file.read(20))  #读出后续的20字符

    file.close()      #文件操作完成，务必关闭


def write_text():
    file = open('/Users/karey/PycharmProjects/new1/test.txt','a+')
    file.write('hello 这是python写的内容.\n')
    file.close()


#并没有专门的修改方法，只能先读，读取后对整个内容进行修改，然后再写回（覆盖的方式w+)
def modify_text():
    file = open('/Users/karey/PycharmProjects/new1/test.txt',mode='r',encoding='utf-8')
    lines = file.readlines()
    lines[2] = '只能写，从文件底部添加内容，不存在则创建.\n'
    print(lines)
    file.close()

    # file = open('/Users/karey/PycharmProjects/new1/test.txt',mode='w',encoding='utf-8')
    # file.writelines(lines)
    # file.close()


#用文本文件保存账户信息 ，账户可以注册(新增)，账户有多个字段，用户名，密码，余额，电话，(标准的二维表)
#如何使用一个文本文件来表示二维表结构的数据

#新增账户时，直接按照csv的格式和字段顺序追加写入a+
#修改余额，先读取文本文件内容到列表，再根据当前用户找到列表中对应的那一行进行修改，而后整体覆盖写回。（性能不高）、
#转账存款取款，均需要操纵修改余额，当然也可以修改密码和手机号
#对于历史操作流水，可以新增一个文件，并且将用户名与用户账户进行关联查找

def woniu_atm_test():
