'''
购物商城接口
'''
from lib import common
from db import db_hanlder
from interface import bank_interface
logger = common.get_logger(__name__)


def shopping_interface(username, shop_car):
    cost = 0
    for v in shop_car.values():
        cost += v[0] * v[1]
    return bank_interface.pay_interface(username, cost)


def add_shop_car_interface(username, shop_car):
    usr_dict = db_hanlder.select(username)
    exist_shop_car = usr_dict['shop_car']
    for k, v in shop_car.items():
        if exist_shop_car.get(k):
            exist_shop_car[k][1] += v[1]
        else:
            exist_shop_car.update({k: v})


def check_shop_car_interface(username):
    usr_dict = db_hanlder.select(username)
    return usr_dict['shop_car']
