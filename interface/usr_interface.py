'''
逻辑接口层
    用户接口
'''
from db import db_hanlder
from lib import common
logger = common.get_logger(__name__)


def register_interface(username, password, balance=15000):
    usr_dict = {
        'username': username,
        'password': common.get_pwd_md5(password),
        'balance': balance,
        'flow': [],
        'shop_car': [],
        'locked': False,
    }
    if db_hanlder.select(username):
        return False, "该用户名已存在"
    else:
        db_hanlder.save(usr_dict)
        msg = f'用户{username}注册成功'
        logger.info(f'用户{username}注册成功')
        return True, msg


def login_interface(username, password):
    from core import src
    usr_dict = db_hanlder.select(username)
    if not usr_dict:
        return False, "该用户不存在，登录失败"
    if usr_dict.get('locked'):
        return False, "该账户被冻结，登陆失败"
    if common.get_pwd_md5(password) == usr_dict.get('password'):
        src.login_usr = username
        msg = f"用户[{src.login_usr}]登录成功"
        logger.info(msg)
        return True, msg
    else:
        return False, "密码错误，登录失败"


def check_bal_interface(username):
    usr_dict = db_hanlder.select(username)
    return usr_dict.get('balance')