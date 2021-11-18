'''
数据处理层
    - 专门用于处理数据的
'''
import json
import os.path

from conf import settings


def select(username):
    usr_path = f'{os.path.join(settings.USER_DATA_PATH, username)}.json'
    if os.path.exists(usr_path):
        with open(usr_path, 'rt', encoding='utf-8') as f:
            usr_info = json.load(f)
            return usr_info


def save(usr_dict):
    username = usr_dict.get('username')
    usr_path = f'{os.path.join(settings.USER_DATA_PATH, username)}.json'
    with open(usr_path, 'wt', encoding='utf-8') as f:
        json.dump(usr_dict, f, ensure_ascii=False)
