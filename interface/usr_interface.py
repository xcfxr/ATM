'''
逻辑接口层
    用户接口
'''
from db import db_hanlder

def register_interface(username, password, balance):
    usr_dict = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car': [],
        'locked': False,
    }
    if db_hanlder.select(username):
        return False, "该用户名已存在"
    else:
        db_hanlder.save(usr_dict)
        return True, f'用户{username}注册成功'