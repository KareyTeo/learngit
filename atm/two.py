#今日练习
# woniuATM功能性需求：
# 1.用户可以自行注册（开户），可以登录。账户不允许重复，必须唯一。
# 2.操作菜单
# 3.查询余额或基本开户信息
# 4.转账：到其他账户，需要确认账户是否存在
# 5.存款 ，取款，
# 6.保存流水信息，且可打印

#两个列表,在内存里运行
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
        start()


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


#构建菜单
def start():
    tip = '''
        ********欢迎来到woniuATM********
        ********请选择操作菜单***********
        ********1.注册 2.登录 3.退出*****
    '''
    print(tip)
    option = input("请输入你的操作选项:")
    if option == "1":
        reg()
    elif option == "2":
        login()
    else:
        exit()


start()





