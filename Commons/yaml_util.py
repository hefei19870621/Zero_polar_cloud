# _*_ coding:utf-8 _*_

"""
@Author:何飞
@File:yaml_util.py
@Time:2022/4/22 9:31
"""
import os
import yaml


# 获取项目根目录
def get_object_path():
    '''
    os.path.dirname(__file__) 获取当前执行脚本的绝对路径
    os.path.dirname(os.path.dirname(__file__)) 获取上一级路径
    os.path.dirname（os.path.dirname(os.path.dirname(__file__)) 获取上二级路径）
    :return:
    '''
    # 设置成绝对路径
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# 读取extract.yaml
def read_extract_yaml(data):
    with open(get_object_path() + "/extract.yaml", mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[data]


# 写入extract.yaml
def write_extract_yaml(data):
    with open(get_object_path() + "/extract.yaml", mode='a', encoding='utf-8') as f:
        # yaml.dump(data=data, stream=f, allow_uncode=True)
        yaml.dump(data=data, stream=f)


# 清空extract.yaml
def clear_extract_yaml():
    with open(get_object_path() + "/extract.yaml", mode='w', encoding='utf-8') as f:
        f.truncate()


# 读取config.yaml
def read_config_yaml(one_node, two_node):
    with open(get_object_path() + "/config.yaml", mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[one_node][two_node]


# 写入stream_media.yaml
def write_stream_media_yaml(data):
    with open(get_object_path() + "/stream_media.yaml", mode='a', encoding='utf-8') as f:
        # yaml.dump(data=data, stream=f, allow_uncode=True)
        yaml.dump(data=data, stream=f)


# 清空stream_media
def clear_stream_media():
    with open(get_object_path() + "/stream_media.yaml", mode='w', encoding='utf-8') as f:
        f.truncate()


if __name__ == '__main__':
    print(get_object_path())
    # write_extract_yaml('"access_token":"(.+?)"')
