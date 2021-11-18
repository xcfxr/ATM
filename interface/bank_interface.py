'''
银行相关业务的接口
'''
from db import db_hanlder
from lib import common
logger = common.get_logger(__name__)


def withdraw_interface(username, amount):
    usr_dict = db_hanlder.select(username)
    balance = usr_dict['balance']
    if amount * 1.05 > balance:
        return False, "余额不足"
    else:
        balance -= amount * 1.05
        usr_dict['balance'] = balance
        flow = f"用户{username}提现[{amount}]元，手续费为[{amount*0.05}]"
        logger.info(flow)
        usr_dict['flow'].append(flow)
        db_hanlder.save(usr_dict)
        return True, flow


def transfer_interface(login_usr, to_usr, amount):
    to_usr_dict = db_hanlder.select(to_usr)
    if not to_usr_dict:
        return False, f"目标用户{to_usr}不存在"
    usr_dict = db_hanlder.select(login_usr)
    if usr_dict['balance'] < amount:
        return False, "当前余额不足， 无法转账"
    usr_dict['balance'] -= amount
    to_usr_dict['balance'] += amount
    usr_flow = f"用户[{login_usr}]给[{to_usr}]转账[{amount}]元"
    logger.info(usr_flow)
    to_usr_flow = f"用户[{to_usr}]接收[{login_usr}]转账[{amount}]元"
    logger.info(to_usr_flow)
    usr_dict['flow'].append(usr_flow)
    to_usr_dict['flow'].append(to_usr_flow)
    db_hanlder.save(usr_dict)
    db_hanlder.save(to_usr_dict)
    return True, usr_flow


def repay_interface(username, amount):
    usr_dict = db_hanlder.select(username)
    usr_dict['balance'] += amount
    msg = f"用户{username}还款[{amount}]元"
    usr_dict['flow'].append(msg)
    logger.info(msg)
    db_hanlder.save(usr_dict)
    return True, msg


def check_flow_interface(username):
    usr_dict = db_hanlder.select(username)
    return usr_dict['flow']


def pay_interface(username, amount):
    usr_dict = db_hanlder.select(username)
    if usr_dict['balance'] > amount:
        usr_dict['balance'] -= amount
        db_hanlder.save(usr_dict)
        msg = f'用户{username}消费了{amount}元'
        logger.info(msg)
        return True, msg
    else:
        return False, f'余额不足，消费失败'
