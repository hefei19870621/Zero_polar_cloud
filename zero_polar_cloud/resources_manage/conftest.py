"""
@Filename:  /conftest
@Author:    何飞
@Time:      2022/5/17 11:25
"""
import pytest

from Commons.mongdb_util import MongDB
from Commons.parametrize import read_testcase_yaml
from Commons.requests_util import RequestsUtil
from Hotloads.debug_talk import DebugTalk



@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    caseinfo = read_testcase_yaml("./zero_polar_cloud/zero_cloud_login.yaml")
    RequestsUtil(DebugTalk()).standard_yaml_testcase(caseinfo)

@pytest.fixture(scope="session")
def del_idc_house():
    db = MongDB("idc_house")
    db.del_one({"house_name": "湖北机房"})
    db.del_one({"house_name": "湖南机房"})
    yield
    db.del_one({"house_name": "湖北机房"})
    db.del_one({"house_name": "湖南机房"})

@pytest.fixture(scope="session")
def del_idc_cabinet():
    db = MongDB("idc_cabinet")
    db.del_one({"cabinet_name": "广西1柜"})
    db.del_one({"cabinet_name": "广西2柜"})
    yield
    db.del_one({"cabinet_name": "广西1柜"})
    db.del_one({"cabinet_name": "广西2柜"})

if __name__ == '__main__':
    # get_login_token()
    del_idc_house()
