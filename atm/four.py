# woniuATM功能性需求：
# 1.用户可以自行注册（开户），可以登录。账户不允许重复，必须唯一。
# 2.操作菜单
# 3.查询余额或基本开户信息
# 4.转账：到其他账户，需要确认账户是否存在
# 5.存款 ，取款，
# 6.保存流水信息，且可打印。账号、何时、操作、金额


# 7.请完善实现基于列表+字典的所有功能及输入校验。
# 8.如有可能，请基于上述代码继续实现流水记录，并可查询（如何支持多条？字符串处理
#   函数split(),流水中如何将日期和时间显示出来 import time ）。
#   9.如有可能，请尝试利用python操作文本文件，来重构
#   10.如有可能，请尝试利用python操作Excel文件，来重构
#   11.如有可能，请尝试利用python操作mysql文件，来重构


#以列表+字典的方式定义账户信息，目前是存在内存中
user_list = [{'username':'bob','password':'666','phonenumber':'18788887777','balance':2000},
             {'username':'ann','password':'6666','phonenumber':'18788886666','balance':3000}]

#定义一个全局变量，用来保存当前登录用户的下标，转账和查询都需要用。默认未登录的情况下为-1
login_index = -1

#注册
def reg():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    phonenumber = input('请输入手机号')

    if  check_user(username) >= 0:
        print('您注册的用户名已存在')

    else:
        print('恭喜你用户名可用')
        user_info = {}
        user_info['username'] = username
        user_info['password'] = password
        user_info['phonenumber'] = phonenumber
        user_info['balance'] = 0


        user_list.append(user_info)
        print('恭喜你注册成功')
        startmenu()

def login():
    username = input('请输入用户名：')
    password = input('请输入密码：')

    index = check_user(username)
    if index >= 0:
        if user_list[index]['password'] == password:
            print('恭喜你登录成功')
            global login_index   #要在函数体中修改全局 变量，则必须加global进行事先声明，如果不修改只读，只可以直接读取
            login_index = index   #修改全局变量login_index为当前登录用户的下标
            main_menu()
        else:
            print('抱歉密码错误')
    else:
        print('抱歉用户名不存在')

#查询
def query():
    balance = user_list[login_index]['balance']
    phone = user_list[login_index]['phonenumber']
    print("你的余额为： %d 元，电话号码为： %s." % (balance, phone))
    main_menu()

#存款
def deposite():
    user_info = user_list[login_index]
    money = input('请输入你存入的钱:')
    if check_number(money):
        check_balance(login_index,int(money))
    else:
        print('请输入正确的金额')
        deposite()   #递归调用重新存钱

#取款，判断取款金额是否大于余额
def withdraw():
    user_info = user_list[login_index]
    money = input('请输入你取出的钱:')
    if check_number(money) and user_info['balance'] >= int(money):
        check_balance(login_index, int(money) * -1)
    else:
        print('请输入正确的金额')
        withdraw()  # 递归调用重新存钱


#转账,注意转账账号是否存在，转账金额少于余额，判断转账成功.a账户和账户
def transfer():
    print('转账正在进行')
    username =  input('请输入对方账户')
    money = input('请输入转账金额')
    to_index = check_user(username)
    if to_index == -1:
        print('对方账户不存在')
        transfer()
    else:
        if check_number(money):
            check_balance(login_index, int(money) * -1)
            check_balance(to_index, int(money))
        else:
            print('请输入正确金额')



#账户余额操作
def check_balance(user_index,money):
    user_info = user_list[user_index]
    user_info['balance'] = user_info['balance'] + money
    user_list[login_index] = user_info
    if money < 0:
        print('恭喜，成功取款：%s 元，当前余额为：%d 元.' % (-money, user_info['balance']))
    else:
        print('恭喜，成功存款：%s 元，当前余额为：%d 元.' % (money, user_info['balance']))
    main_menu()



#流水
def query_history():




















def check_user(username):
    '检查用户名是否存在，存在返回下标i，不存在返回-1'
    for i in range(len(user_list)):
        if user_list[i]['username'] == username:
            return i
    return -1

#对输入的字符串进行判断，确认其是否可以转换为一个有效的数字
def check_number(string):
    point = 0
    is_valid = True
    for c in string:
        code = ord(c)
        if (code < 48 and code != 46) or code >57:
            is_valid =False
            break
        elif code ==46:point += 1

    if point > 1: is_valid = False

    return is_valid




#构建菜单
def startmenu():
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
    if option == '3':
        deposite()
    if option == '2':
        withdraw()

startmenu()