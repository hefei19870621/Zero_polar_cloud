"""
@Filename:  Datas/zero_polar_cloud/resources_manage/resources_manage
@Author:    何飞
@Time:      2022/5/19 10:43
"""

import allure
import pytest

from Commons.parametrize import read_testcase_yaml
from Commons.requests_util import RequestsUtil
from Hotloads.debug_talk import DebugTalk


@allure.epic("零极云运维管理系统")
@allure.feature("冒烟回归")
@pytest.mark.usefixtures("del_idc_house")
class Test_smoke_case:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("/zero_polar_cloud/smoke_case/smoke_case.yaml"))
    @allure.title("{caseinfo[case_name]}")
    @pytest.mark.smoke
    def test_add_house(self, caseinfo):
        RequestsUtil(DebugTalk()).standard_yaml_testcase(caseinfo)