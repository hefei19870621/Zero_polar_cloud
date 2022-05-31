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
    db.del_one({"house_name": "河南机房"})
    yield
    db.del_one({"house_name": "河南机房"})

@pytest.fixture(scope="session")
def del_idc_cabinet():
    db = MongDB("idc_cabinet")
    db.del_one({"cabinet_name": "河南机柜"})
    yield
    db.del_one({"cabinet_name": "河南机柜"})

if __name__ == '__main__':
    # get_login_token()
    del_idc_house()
