'''
存放用户视图层
'''

from interface import usr_interface
from interface import bank_interface
from interface import shop_interface
from lib import common
login_usr = None


# 1、注册功能
def register():
    while True:
        username = input('请输入用户名(温馨提示：按q退出)：')
        if username == 'q':
            break
        pwd = input('请输入密码：')
        re_pwd = input('请确定密码：')
        if pwd == re_pwd:
            flag, msg = usr_interface.register_interface(username, re_pwd)
            if flag:
                print(msg)
                break
            else:
                print()


# 2、购物功能
@common.login_auth
def shopping():
    shop_list = [
        ['上海灌汤包', 30],  # 0
        ['矮跟写真抱枕', 250],  # 1
        ['广东凤爪', 28],
        ['香港地道鱼丸', 15],
        ['坦克', 100000],
        ['macbook', 20000],
    ]
    shop_car = {}
    while True:
        for idx, shop_info in enumerate(shop_list):
            print(f'商品编号{idx}，商品名称：{shop_info[0]}，商品单价：{shop_info[1]}')
        choice = input('请选择购买的商品，是否结账请输入y或n：')
        if choice == 'y':
            if not shop_car:
                print('结账失败，购物车为空')
                continue
            shop_interface.shopping_interface(login_usr, shop_car)
            break
        if choice == 'n':
            if not shop_car:
                print('结账失败，购物车为空')
                continue
            shop_interface.add_shop_car_interface(login_usr, shop_car)
            print('添加购物车成功')
            break

        choice = int(choice)
        name, price = shop_list[choice]
        if shop_car.get(name):
            shop_car[name][1] += 1
        else:
            shop_car[name] = [price, 1]
        print(f'添加成功，当前购物车为{shop_car}')


# 3、提现功能
@common.login_auth
def withdraw():
    while True:
        amount = input("请输入提现金额(温馨提示：按q退出)：").strip()
        if not amount.isdigit():
            print('金额有误，请重新输入')
        amount = int(amount)
        flag, msg = bank_interface.withdraw_interface(login_usr, amount)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 4、登录功能
def login():
    while True:
        username = input('请输入用户名(温馨提示：按q退出)：')
        if username == 'q':
            break
        pwd = input('请输入密码：')
        flag, msg = usr_interface.login_interface(username, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5、还款功能
@common.login_auth
def repay():
    while True:
        amount = input('请输入还款金额(温馨提示：按q退出)：').strip()
        if not amount.isdigit():
            print('还款金额必须是数字， 请重新输入')
            continue
        amount = int(amount)
        if amount < 0:
            print('还款金额必须是正数，请重新输入')
            continue
        bank_interface.repay_interface(login_usr, amount)


# 6、查看流水
@common.login_auth
def check_flow():
    flows = bank_interface.check_flow_interface(login_usr)
    if flows:
        for flow in flows:
            print(flow)
    else:
        print(f'当前用户[{login_usr}]暂无流水')


# 7、管理员功能
@common.login_auth
def admin():
    from core import admin
    admin.admin_run()


# 8、转账功能
@common.login_auth
def transfer():
    while True:
        to_usr = input('请输入转账对象(温馨提示：按q退出)：')
        amount = input('请输入转账金额：')
        if not amount.isdigit():
            print('转账金额必须是数字， 请重新输入')
            continue
        amount = int(amount)
        if amount < 0:
            print('转账金额必须是正数，请重新输入')
            continue
        flag, msg = bank_interface.transfer_interface(login_usr, to_usr, amount)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 9、查看购物车功能
@common.login_auth
def check_shop_car():
    shop_car = shop_interface.check_shop_car_interface(login_usr)
    if shop_car:
        print(shop_car)
    else:
        print('查看购物车失败，当前购物车为空')


# 10、查看余额
@common.login_auth
def check_balance():
    balance = usr_interface.check_bal_interface(login_usr)
    print(f'当前用户[{login_usr}]的余额为{balance}元')


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
        ============end============
              ''')
        choice = input('请输入功能编号(温馨提示：按q退出)：')
        if choice == 'q':
            break
        if choice not in func_dict:
            print('请输入正确的功能编号！')
        func_dict.get(choice)()
