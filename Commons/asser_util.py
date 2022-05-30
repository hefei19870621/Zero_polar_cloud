"""
@Filename:  Commons/asser_util
@Author:    何飞
@Time:      2022/5/20 11:26
"""
import traceback
import jsonpath
from Commons.logger_util import logs, error_log


# 断言判断
def assert_result(yq_result, sj_result, status_code):
    try:
        all_flag = 0
        for yq in yq_result:
            for key, value in yq.items():
                if key == "status_code":
                    flag = status_code_assert(value, status_code)
                    all_flag = all_flag + flag
                elif key == "equals":
                    flag = equals_assert(value, sj_result)
                    all_flag = all_flag + flag
                elif key == "contains":
                    flag = contains_assert(value, sj_result)
                    all_flag = all_flag + flag
                else:
                    error_log("框架暂不支持此断言方式")
        if all_flag == 0:
            logs("结果断言成功！")
        elif all_flag == -1:
            logs("没有断言！")
        else:
            logs("结果断言失败！")
            assert 1 == 2
    except Exception as e:
        error_log("断言方法assert_result异常：%s" % str(traceback.format_exc()))
        raise e


# 状态断言
def status_code_assert(value, status_code):
    flag = 0
    for assert_key, assert_value in value.items():
        if assert_key == "status_code":
            if assert_value != status_code:
                flag = flag + 1
                error_log("状体码断言失败：返回的状态码不等于%s" % assert_value)
    return flag


# 相等断言
def equals_assert(value, sj_result):
    flag = 0
    for assert_key, assert_value in value.items():
        # $..匹配的相对路径
        lists = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
        if lists:
            if assert_value not in lists:
                flag = flag + 1
                error_log("相等断言失败：" + str(assert_key) + "不等于" + str(assert_value))
        else:
            error_log("相等断言失败：返回的结果中不存在：" + assert_key)
    return flag


# 包含断言
def contains_assert(value, sj_result):
    flag = 0
    if str(value) not in str(sj_result):
        flag = flag + 1
        error_log("包含断言失败：返回的结果中不包含：%s" % str(value))
    return flag
