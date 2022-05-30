"""
@Filename:  Commons/mongdb_util
@Author:    何飞
@Time:      2022/5/18 18:10
"""
import os

import pymongo

# conn = pymongo.MongoClient('mongodb://root:123456@192.168.3.248:27017')
# db_name = 'lj_web'
# collection_name = 'idc_house'
# database = conn[db_name]
# collection = database[collection_name]
# x = collection.find_one({})
# for key, value in x.items():
#     print(str(key)+"=="+str(value))
from Commons.yaml_util import read_config_yaml


class MongDB:

    def __init__(self, collection):
        username = read_config_yaml("mongdb_db", "username")
        password = read_config_yaml("mongdb_db", "password")
        host = read_config_yaml("mongdb_db", "host")
        port = read_config_yaml("mongdb_db", "port")
        db_name = read_config_yaml("mongdb_db", "db_name")
        self.conn = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}'.format(username, password, host, port))
        self.db = self.conn[db_name]
        self.collection = self.db[collection]

    def add_one(self, data):
        """
        添加一条数据
        data:字典
        """
        return self.collection.insert_one(data)

    def add_many(self, data):
        """
        添加多条
        data:包含字典的列表
        """
        return self.collection.insert_many(data)

    def get_one(self):
        """获取一条数据"""
        return self.collection.find_one()

    def get_many(self):
        """获取多条数据"""
        return self.collection.find()

    def get_data(self, data):
        """通过条件获取"""
        for i in self.collection.find(data):
            return i

    def up_one(self, query, data):
        """单条更新"""
        return self.collection.update_one(query, data)

    def up_many(self, query, data):
        """多条更新"""
        result = self.collection.update_many(query, data, True)

    def del_one(self, query):
        """
        删除单数据
        删除第一个满足条件的数据"""
        return self.collection.delete_one(query)

    def del_many(self, query):
        """
        删除多条
        删除所有满足条件的数据"""
        return self.collection.delete_many(query)

    def close(self):
        """关闭连接"""
        self.conn.close()


if __name__ == '__main__':

    db = MongDB("idc_house")
    print(db.get_one())
    print(db.get_data({'area': '广东'}))

    for i in db.get_many():
        for k, j in i.items():
            print(k, j)

    # 添加
    # mdb.add_one({"title": "java", "content": "教育"})
    # dt = [
    #     {"title": "c++", "content": "C++"},
    #     {"title": "php", "content": "PHP"},
    # ]
    # mdb.add_many(dt)

    # 获取
    # result = mdb.get_one()
    # print(result)
    # 获取多条
    # res = mdb.get_many()
    # for da in res:
    #     print(da)

    # 条件获取
    # query = {"title": "python"}
    # res = mdb.get_data(query)
    # for da in res:
    #     print(da)

    # 通过_id查询导入包from bson.objectid import ObjectId
    # query = {"_id": ObjectId("625410ab39d8d7eec64e2c90")}
    # res = mdb.get_data(query)
    # for da in res:
    #     print(da)

    # 更新一条
    # q = {"title": "php"}
    # d = {"$set": {"title": "c#", "content": "C#"}}
    # mdb.up_one(q, d)

    # 更新多条
    # q = {"title": "php"}
    # d = {"$set": {"title": "python", "content": "MongoDB"}}
    # mdb.up_many(q, d)

    # 删除单条
    # q = {"house_name": "九江机房"}
    # mdb.del_one(q)

    # 删除多条
    q = {"area": {"$regex": "广东"}}
    # mdb.del_many(q)
