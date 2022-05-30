"""
@Filename:  /conftest
@Author:    何飞
@Time:      2022/5/17 11:25
"""
import pytest
from Commons.yaml_util import clear_stream_media, clear_extract_yaml
from Hotloads.debug_talk import DebugTalk

@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_extract_yaml()

@pytest.fixture(scope="session")
def clear_extract():
    clear_stream_media()
    DebugTalk().create_streamID()
    DebugTalk().create_timeStamp()
    DebugTalk().create_ZDAN_Token()
