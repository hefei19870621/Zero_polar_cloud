"""
@Filename:  /resources_manage_run
@Author:    何飞
@Time:      2022/5/19 10:46
"""

import os

import pytest

if __name__ == '__main__':
    pytest.main(['-m','smoke'])
    os.system("allure generate /reports/allure -o ./reports/html --clean")