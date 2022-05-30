# _*_ coding:utf-8 _*_

"""
@Author:何飞
@File:parametrize.py
@Time:2022/4/27 14:27
"""
import json
import traceback
import yaml
from Commons.logger_util import error_log, logs
from Commons.yaml_util import get_object_path


# 读取测试用例的yaml文件
def read_testcase_yaml(yaml_path):
    try:
        with open(get_object_path() + yaml_path, mode='r', encoding='utf-8') as f:
            caseinfo = yaml.load(f, Loader=yaml.FullLoader)
            if len(caseinfo) >= 2: # 直接用模板的参数，不使用paramterize参数化
                return caseinfo
            else:
                if "paramterize" in dict(*caseinfo).keys():
                    new_caseinfo = ddt_testcases_yaml(*caseinfo)
                    return new_caseinfo
                else:
                    return caseinfo
    except Exception as e:
        error_log("读取测试用例方法read_testcase_yaml异常：%s" % str(traceback.format_exc()))
        raise e


# 数据驱动测试数据
def ddt_testcases_yaml(caseinfo):
    try:
        caseinfo_str = json.dumps(caseinfo)
        paramterize_list = caseinfo['paramterize']
        length_success = True
        key_length = len(paramterize_list[0])
        for param in caseinfo["paramterize"]:
            if len(param) != key_length:
                length_success = False
                logs("此条数据有误: %s" % param)
            # 替换值
            new_caseinfo = []
            if length_success:
                for x in range(1, len(paramterize_list)):  # 循环数据行数
                    raw_caseinfo = caseinfo_str
                    for y in range(0, len(paramterize_list[x])):  # 循环数据列
                        raw_caseinfo = raw_caseinfo.replace("$ddt{" + paramterize_list[0][y] + "}",
                                                            str(paramterize_list[x][y]))
                    new_caseinfo.append(json.loads(raw_caseinfo))  # 把每一行的字典追加到新的列表里面
            return new_caseinfo
    except Exception as e:
        error_log("数据驱动方法ddt异常：%s" % str(traceback.format_exc()))
        raise e


if __name__ == '__main__':
    f = read_testcase_yaml("/zero_polar_cloud/resources_manage/computer_manage.yaml")
    for i in f:
        print(i['paramterize'])
