# coding=utf-8
from utils import Utils as ut


def run():
    # 获取配置参数
    cfg = ut.get_conf_object("conf.ini")
    sheet_index = ut.get_section_option(cfg, "default", "sheet_index")
    key_col = ut.get_section_option(cfg, "default", "key")
    language_col = ut.get_section_option(cfg, "language", "values-ja")
    # 获取excel表格
    wb = ut.get_wb_exist("./data/languages.xlsx")
    wb_sheet = ut.get_excel_sheet(wb, int(sheet_index))
    max_row = ut.get_sheet_row(wb_sheet)
    # max_col = ut.get_sheet_col(wb_sheet)

    # 新建excel表格
    new_wb = ut.create_excel_sheet()
    new_wb_sheet = ut.get_excel_sheet(new_wb, 0)
    data = ["序号", "key", "预期结果", "实测结果", "测试结果"]
    ut.write_sheet(new_wb_sheet, data)
    # 获取xml
    root = ut.get_xml_root("data/strings.xml")
    for i in range(2, max_row + 1):
        key = ut.get_cell_value(wb_sheet, i, int(key_col))
        key_expect_value = ut.get_cell_value(wb_sheet, i, int(language_col))
        search_value = ut.get_attrib_value(root, key)
        if search_value == key_expect_value:
            result = "PASS"
        else:
            result = "FAIL"
        data = [i-1, key, key_expect_value, search_value, result]
        print(data)
        ut.write_sheet(new_wb_sheet, data)
    ut.save_wb(new_wb, "language_ja_report.xlsx")


if __name__ == "__main__":
    run()
