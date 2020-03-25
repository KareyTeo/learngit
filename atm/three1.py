# 基本要求：利用两个列表，一个放用户名，一个放密码，下标位置对应上。同时注册时，需要确认是否用户名已存在，利用函数来组织代码。
# 扩展要求：把两个列表减少为一个列表，完成同样功能，列表中的列表
# 如果需要存第三个值，如电话号码？请问怎么做比较好


#二维列表,可以扩展列表中的值
user_list = [['q','1','13822347896'],['w','2','12877654789']]
# print(user_list[1][1])
# print(user_list[1][2])
# print(user_list[1][0])

def reg():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    phonenumber = input('请输入手机号')

    if  check(username) >= 0:
        print('您注册的用户名已存在')

    else:
        print('恭喜你用户名可用')
        user_info =[]
        user_info.append(username)
        user_info.append(password)
        user_info.append(phonenumber)

        user_list.append(user_info)
        print('恭喜你注册成功')
        startmenu()



def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')

    index = check(username)
    if index >= 0:
        if user_list[index][1] == password:
            print('恭喜你登录成功')
            main_menu()
        else:
            print('抱歉密码错误')
    else:
        print('抱歉用户名不存在')

#查询
def query():
    pass

#存款
def deposite():
    pass

#取款
def wuthdraw():
    pass

#转账
def transer():
    pass

#流水
def query_history():
    pass




def check(username):
    '检查用户名是否存在，存在返回下标i，不存在返回-1'
    # for i in range(len(user_list)):
    #     if user_list[i][0] == username:
    #         return i
    # return -1

    #二维列表检查
    for user_info in user_list:
        if username in user_info:
            return user_list.index(user_info)
    return -1


#构建菜单
def startmenu():
    tip = '''
        ********欢迎来到woniuATM********
        ********请选择操作菜单*****3
        ******
        ********1.注册 2.登录 3.退出*****
    '''
    print(tip)
    option = input("请输入你的操作选项:")
    if option == "1":
        reg()
    elif option == "2":
        login()
    else:
        exit('欢迎下次光临')


#构建登录后的业务菜单
def main_menu():
    tip = '''
        ********登录成功woniuATM********
        ********请选择操作菜单***********
        ********1.查询 2.取款 3.存款 4.转账 5.流水 6.返回 7.退卡**** 
    '''
    print(tip)
    option = input("请输入你的操作选项:")
    if  option == '7':
        exit('退出成功')




startmenu()