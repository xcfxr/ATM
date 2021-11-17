'''
存放用户视图层
'''

from interface import usr_interface


# 1、注册功能
def register():
    while True:
        username = input('请输入用户名')
        pwd = input('请输入密码')
        re_pwd = input('请确定密码')
        if pwd == re_pwd:
            flag, msg = usr_interface.register_interface(username, re_pwd)
            if flag:
                print(msg)
                break
            else:
                print()


# 2、购物功能
def shopping():
    pass


# 3、提现功能
def withdraw():
    pass


# 4、登录功能
def login():
    pass


# 5、还款功能
def repay():
    pass


# 6、查看流水
def check_flow():
    pass


# 7、管理员功能
def admin():
    pass


# 8、转账功能
def transfer():
    pass


# 9、查看购物车功能
def check_shop_car():
    pass


# 10、查看余额
def check_balance():
    pass


func_dict = {
    '1': register,
    '2': shopping,
    '3': withdraw,
    '5': repay,
    '6': check_flow,
    '7': admin,
    '4': login,
    '8': transfer,
    '9': check_shop_car,
    '10': check_balance,
}


# 视图层主程序
def run():
    while True:
        print(''' 
        =======ATM + 购物车=========
              1、注册功能
              2、购物功能
              3、提现功能
              4、登录功能
              5、还款功能
              6、查看流水
              7、管理员功能
              8、转账功能
              9、查看购物车功能
              10、查看余额
        ==========end===============
              ''')
    choice = input('请输入功能编号：')
    if choice not in func_dict:
        print('请输入正确的功能编号！')
    func_dict.get(choice)()
