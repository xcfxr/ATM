import hashlib
import logging.config
from functools import wraps
from core import src
from conf import settings


def get_pwd_md5(password):
    md5_object = hashlib.md5()
    md5_object.update(password.encode('utf-8'))
    md5_object.update("lucky_man".encode('utf-8'))
    return md5_object.hexdigest()


def login_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if src.login_usr:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录，先将跳转登录界面")
            src.login()
    return wrapper


def get_logger(log_name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    return logging.getLogger(log_name)
