from core import src
from interface import admin_interface


def change_balance():
    while True:
        username = input("请输入需要修改金额的用户(温馨提示：按q退出)：").strip()
        amount = input("请输入要修改的金额：").strip()
        flag, msg = admin_interface.change_bal_interface(username, amount)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def frozen_usr():
    while True:
        username = input("请输入需要冻结的用户(温馨提示：按q退出)：").strip()
        flag, msg = admin_interface.frozen_usr_interface(username)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def add_usr():
    src.register()


admin_func_dic = {
    '1': add_usr,
    '2': change_balance,
    '3': frozen_usr,
}


def admin_run():
    while True:
        print('''
        温馨提示：按q退出
        =======管理员功能编号=======
                1.添加账户
                2.修改用户额度
                3.冻结账户
        ==========end==============
        ''')
        choice = input("请输入选择的编号(温馨提示：按q退出)：")
        if choice == 'q':
            break
        if choice in admin_func_dic:
            admin_func_dic[choice]()
        else:
            print('请输入正确的编号')
            continue
