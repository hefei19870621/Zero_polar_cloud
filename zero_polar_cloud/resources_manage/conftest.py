"""
@Filename:  /conftest
@Author:    何飞
@Time:      2022/5/17 11:25
"""
import pytest

from Commons.mongdb_util import MongDB

db = MongDB("idc_house")

@pytest.fixture(scope="session")
def del_idc_house():
    db.del_one({"house_name": "湖北机房"})
    db.del_one({"house_name": "湖南机房"})
    yield
    db.del_one({"house_name": "湖北机房"})
    db.del_one({"house_name": "湖南机房"})

if __name__ == '__main__':
    # get_login_token()
    del_idc_house()
