
# 基本要求：利用两个列表，一个放用户名，一个放密码，下标位置对应上。同时注册时，需要确认是否用户名已存在，利用函数来组织代码。
# 扩展要求：把两个列表减少为一个列表，完成同样功能，列表中的列表
# 如果需要存第三个值，如电话号码？请问怎么做比较好


user_list = ['q',]
pass_list = [1,]
#往列表中写数据，注册
def reg():
    username = input('请输入用户名：')
    passport = input('请输入密码：')

    if check(username) >= 0:
        print('你注册的用户名已存在')
    else:
        #print("恭喜你，用户名可用")
        user_list.append(username)
        pass_list.append(passport)
        print('恭喜你，注册成功')

#从列表中读数据
def login():
    username = input('请输入用户名：')
    passport = input('请输入密码：')

    index = check(username)
    if index >= 0:
        if pass_list[index] == passport:
            print('恭喜你，登录成功')
        else:
            print('抱歉，密码输入错误')
    else:
        print('用户名不存在')
        #login()     #或递归调用自身，实现死循环

def check(username):
    '''
    检查用户名是否存在，存在返回下标，不存在返回-1
    '''
    for i in range(len(user_list)):
        if user_list[i] == username:
            return i

    return -1

#根据用户名寻找下标
# def find(username):
#     for i in range(len(user_list)):
#         if user_list[i] == username:
#             return i
#     return -1

reg()
login()
