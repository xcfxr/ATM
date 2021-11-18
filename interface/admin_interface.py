from db import db_hanlder
import logging.config
from conf import settings
from lib import common
logger = common.get_logger(__name__)


def frozen_usr_interface(username):
    usr_dict = db_hanlder.select(username)
    if usr_dict:
        usr_dict['locked'] = True
        db_hanlder.save(usr_dict)
        return True, f'用户[{username}]已被冻结'
    else:
        return False, f'用户[{username}]不存在'


def change_bal_interface(username, balance):
    usr_dict = db_hanlder.select(username)
    if usr_dict:
        usr_dict['balance'] = balance
        db_hanlder.save(usr_dict)
        return True, f'用户[{username}]的金额已被修改为{balance}'
    else:
        return False, f'用户[{username}]不存在'