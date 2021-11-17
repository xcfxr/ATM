'''
存放配置信息
'''
import os.path

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_PATH, 'db')

USER_DATA_PATH = os.path.join(DB_PATH, 'user_data')