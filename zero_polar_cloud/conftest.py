"""
@Filename:  /conftest
@Author:    何飞
@Time:      2022/5/17 11:25
"""
import pytest

from Commons.mongdb_util import MongDB
from Commons.parametrize import read_testcase_yaml
from Commons.requests_util import RequestsUtil
from Commons.yaml_util import clear_extract_yaml
from Hotloads.debug_talk import DebugTalk

db = MongDB("idc_house")

# @pytest.fixture(scope="session", autouse=True)
# def clear_extract():
#     clear_extract_yaml()

@pytest.fixture(scope="session", autouse=True)
def get_login_token():
    caseinfo = read_testcase_yaml("./zero_polar_cloud/zero_cloud_login.yaml")
    RequestsUtil(DebugTalk()).standard_yaml_testcase(caseinfo)

if __name__ == '__main__':
    get_login_token()
