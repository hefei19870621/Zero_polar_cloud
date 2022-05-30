"""
@Filename:  /run
@Author:    何飞
@Time:      2022/5/17 11:25
"""

import os

import pytest

if __name__ == '__main__':
    pytest.main([])
    os.system("allure generate ./reports/allure -o ./reports/html --clean")