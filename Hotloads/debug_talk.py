# _*_ coding:utf-8 _*_

"""
@Author:何飞
@File:debug_talk.py
@Time:2022/4/25 10:58
"""
import datetime
import hashlib
import random

import yaml
from faker import Faker

from Commons.yaml_util import get_object_path, write_stream_media_yaml

faker=Faker(locale="zh_CN")
class DebugTalk:
    # 获取随机数
    def get_random_number(self, num):
        return "".join("%s" % random.randint(0, 9) for _ in range(int(num)))

    # 读取全局变量文件
    def read_extract_data(self, key):
        with open(get_object_path() + "./extract.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
        return value[key]

    # 读取config.yaml
    def read_config_yaml(self,one_node, two_node):
        with open(get_object_path() + "./config.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[one_node][two_node]

    # 读取stream_media_yaml.yaml
    def read_stream_media_yaml(self,data):
        with open(get_object_path() + "./stream_media.yaml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value[data]

    def create_streamID(self):
        streamID1 = "".join("%s" % random.randint(0, 9) for _ in range(9))
        streamID2 = "hf"
        StreamID = streamID2 + streamID1
        value = {"StreamID": StreamID}
        return write_stream_media_yaml(value)

    def create_timeStamp(self):
        later_days = datetime.datetime.now() + datetime.timedelta(days=5)
        timeStamp = "{}".format(int(later_days.timestamp()))
        value = {"TimeStamp": timeStamp}
        return write_stream_media_yaml(value)

    def create_ZDAN_Token(self):
        StreamID = self.read_stream_media_yaml("StreamID")
        timeStamp = self.read_stream_media_yaml("TimeStamp")
        password = "aaaabbbccc"
        str_datas = password + StreamID + timeStamp
        m = hashlib.md5()
        m.update(str_datas.encode('UTF-8'))
        ZDAN_Token = m.hexdigest().upper()
        value = {"ZDAN_Token": ZDAN_Token}
        return write_stream_media_yaml(value)

    def create_name(self):
        return faker.name()

    def create_province(self):
        return faker.province()

    def create_city_name(self):
        return faker.city_name()
if __name__ == '__main__':

    print(DebugTalk().read_extract_data("access_token"))
    print(DebugTalk().read_config_yaml("base",'zero_polar_cloud'))
