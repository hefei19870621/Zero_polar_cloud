"""
@Filename:  /conftest
@Author:    何飞
@Time:      2022/5/17 11:25
"""
import pytest

from Commons.yaml_util import clear_extract_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_yaml()



if __name__ == '__main__':
    clear_extract()
