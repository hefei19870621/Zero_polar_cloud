"""
@Filename:  /resources_manage_run
@Author:    何飞
@Time:      2022/5/19 10:46
"""
import pymongo
import os

from Commons.yaml_util import read_config_yaml

'''
pip install pymongo
'''

class MbConnect:
    """创建一个链接mongodb的类"""

    def __init__(self, collection):
        username = read_config_yaml("db", "username")
        password = read_config_yaml("db", "password")
        host = read_config_yaml("db","host")
        port = read_config_yaml("db","port")
        db_name = read_config_yaml("db","db_name")

        # 创建MongoDB的连接对象
        self.client = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format(username,password,host,port))
        # 声明一个database对象（指定连接的数据库）
        self.db = self.client[db_name]
        # 声明一个Collection对象（指定集合）
        self.col = self.db[collection]

    def insert(self, data, ins_var=True):
        """插入数据"""
        if ins_var:
            one = self.col.insert_one(data)
            # insert()方法会在执行后返回InsertOneResult对象,调用其inserted_id属性获取_id
            return one
        else:
            many = self.col.insert_many(data)
            # 插入多条数据时，以列表形式入参
            return many

    def find(self, data, find_var=True):
        """查询数据, 如果查询结果不存在，则会返回None"""
        if find_var:
            result = self.col.find_one(data)
            return result
        else:
            result = self.col.find(data)
            # find()返回一个生成器对象
            return result

    def count(self, data):
        """查询数据的总条数"""
        result = self.col.count_documents(data)
        return result

    def delete(self, data, del_var=True):
        """删除数据，调用deleted_count属性获取删除的数据条数"""
        if del_var:
            result = self.col.delete_one(data)
            return result
        else:
            result = self.col.delete_many(data)
            print(result)
            return result

    def close(self):
        """关闭连接"""
        self.client.close()


def mg_insert(collection, data, ins_var=True):
    """插入数据"""
    try:
        db = MbConnect(collection)
        result = db.insert(data, ins_var)
        db.close()
        return result
    except Exception as info:
        print("连接数据库异常：%s" % info)


def mg_find(collection, data, ins_var=True):
    """查询数据库"""
    try:
        db = MbConnect(collection)
        result = db.find(data, ins_var)
        db.close()
        return result
    except Exception as info:
        print("连接数据库异常：%s" % info)


def mg_count(collection, data):
    """查询数据的总条数"""
    try:
        db = MbConnect(collection)
        result = db.count(data)
        db.close()
        return result
    except Exception as info:
        print("连接数据库异常：%s" % info)


def mg_delete(collection, data, ins_var=True):
    """清理数据库"""
    try:
        db = MbConnect(collection)
        result = db.delete(data, ins_var)
        db.close()
        return result
    except Exception as info:
        print("连接数据库异常：%s" % info)


if __name__ == '__main__':
    r = mg_count()
    print(r)
