# _*_ coding:utf-8 _*_

"""
@Author:何飞
@File:requests_util.py
@Time:2022/4/22 14:27
"""
import json
import re
import traceback
import jsonpath
import requests

from Commons.asser_util import assert_result
from Commons.logger_util import error_log, logs
from Commons.yaml_util import read_config_yaml, write_extract_yaml


class RequestsUtil:

    def __init__(self, obj):
        self.obj = obj

    # 通过session会话去关联
    session = requests.session()

    # 规范化YAML测试用例
    def standard_yaml_testcase(self, caseinfo):
        logs("-" * 15 + "开始执行用例" + "-" * 15)
        try:
            caseinfo_keys = caseinfo.keys()
            # 判断一级关键字是否包含有：name，requests，validate
            if "case_name" in caseinfo_keys and "requests" in caseinfo_keys and "validate" in caseinfo_keys:
                logs("用例名称：%s" % caseinfo['case_name'])
                # 判断requests下面是否包含：method，url
                requests_keys = caseinfo['requests'].keys()
                if "method" in requests_keys and "base_url" in requests_keys and "url" in requests_keys:
                    # pop根据keys删除值，并返回值
                    caseinfo.pop('case_name')
                    method = caseinfo['requests'].pop('method')
                    base_url = caseinfo['requests'].pop('base_url')
                    url = caseinfo['requests'].pop('url')

                    # 发送请求
                    res = self.send_all_request(method, base_url, url, **caseinfo['requests'])
                    return_text = res.text
                    status_code = res.status_code
                    resturn_json = ""

                    try:
                        resturn_json = res.json()
                    except Exception as e:
                        error_log("返回的结果不是json格式！")
                    # 提取值并且写入extract.yaml文件
                    if "extract" in caseinfo_keys:
                        for key, value in caseinfo["extract"].items():
                            # 正则匹配
                            if "(.+*)" in value or "(.+?)" in value:
                                zz_value = re.search(value, return_text)
                                if zz_value:
                                    extract_value = {key: zz_value.group(1)}
                                    write_extract_yaml(extract_value)
                                else:
                                    error_log("extract提取变量，正则表达式写法有误！")
                            # json提取
                            else:
                                json_value = jsonpath.jsonpath(resturn_json, value)
                                if json_value:
                                    extract_value = {key: json_value[0]}
                                    write_extract_yaml(extract_value)
                                else:
                                    error_log("extract提取变量，JSONPATH写法有误！")
                    # 断言
                    yq_result = caseinfo['validate']
                    logs("预期结果：%s" % yq_result)
                    sj_result = resturn_json
                    logs("实际结果：%s" % sj_result)
                    assert_result(yq_result, sj_result, status_code)

                    logs("-" * 15 + "用例执行成功" + "-" * 15 + "\n")
                else:
                    error_log("在requests下必须包含且等于：method，base_url，url")
            else:
                error_log("一级关键字必须包含且等于：name，requests，paramterize，validate")
        except Exception as e:
            error_log("规范YAML测试用用例方法standard_yaml异常：%s" % str(traceback.format_exc()))
            raise e

    # 统一封装请求
    def send_all_request(self, method, base_url, url, **kwargs):
        logs("请求方式：%s" % method)
        logs("请求路径：%s" % url)
        try:
            # 请求方式处理，转小写
            method = str(method).lower()
            # 基础路径拼接以及替换
            url = self.replace_get_value(base_url + url)
            # 参数的替换
            for key, value in kwargs.items():
                if key in ['params', 'data', 'json', 'headers']:
                    kwargs[key] = self.replace_get_value(value)
                    logs("请求" + key + "参数：%s" % kwargs[key])
                elif key == "files":
                    for file_key, file_path in value.items():
                        logs("请求文件：%s" % kwargs[key])
                        value[file_key] = open(file_path, 'rb')
            # 请求
            res = RequestsUtil.session.request(method, url, **kwargs)
            return res
        except Exception as e:
            error_log("发送请求方法send_request异常：%s" % str(traceback.format_exc()))
            raise e

    # 替换值的方法(替换，url，params，data，json，headers)
    def replace_get_value(self, data):
        try:
            if data:
                # 保存数据类型
                data_type = type(data)
                # 判断数据类型
                if isinstance(data, dict) or isinstance(data, list):
                    str_data = json.dumps(data)
                else:
                    str_data = str(data)
                # 替换
                for cs in range(1, str_data.count('${') + 1):
                    if "${" in str_data and "}" in str_data:
                        start_index = str_data.index("${")
                        end_index = str_data.index("}", start_index)
                        old_value = str_data[start_index:end_index + 1]
                        # 反射：通过类的对象和方法字符串调用方法
                        func_name = old_value[2:old_value.index('(')]
                        args_value1 = old_value[old_value.index('(') + 1:old_value.index(')')]
                        if args_value1 != "":
                            args_value2 = args_value1.split(',')
                            new_value = getattr(self.obj, func_name)(*args_value2)

                        else:
                            new_value = getattr(self.obj, func_name)()
                        # 替换
                        if isinstance(new_value, int) or isinstance(new_value, float):
                            str_data = str_data.replace('"' + old_value + '"', str(new_value))
                        else:
                            str_data = str_data.replace(old_value, str(new_value))
                # 还原数据类型
                if isinstance(data, dict) or isinstance(data, list):
                    data = json.loads(str_data)
                else:
                    data = data_type(str_data)
            else:
                error_log("None不需要通过$替换")
            return data
        except Exception as e:
            error_log("热加载替换方法异常：%s" % str(traceback.format_exc()))
            raise e
