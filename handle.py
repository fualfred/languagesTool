# coding=utf-8
"""
专门处理数据的类
"""


class Handle(object):
    def __init__(self):
        super(Handle, self).__init__()

    """处理excel表格数据"""

    def handle_data(self, get_value, ck_value):
        # get_value = ut.get_attrib_value(get_value, key)
        if "\'" in ck_value:
            ck_value = ck_value.replace("\'", "\\'")
            print(ck_value)
        if get_value == ck_value:
            return "PASS"
        else:
            return "FAIL"

    """返回结果数据"""

    def handle_result_data(self, en_value, en_col, key, ck_value, ck_key, get_value, result, remark, differ):
        return [en_value, en_col, key, ck_value, ck_key, get_value, result, remark, differ]
