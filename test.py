# coding=utf-8
from utils import Utils as ut

root = ut.get_xml_root("data/strings1.xml")
# for stu in root:
#     print("name", stu.attrib["name"])
#     print("value", stu.text)
# value = ut.get_attrib_value(root, "smart_auto")
# print(value)
# keys = ut.get_key_by_value(root, "Auto")
# print(keys)
# wb = ut.get_wb_exist("./data/languages.xlsx")
# sheet = ut.get_excel_sheet(wb, 0)
# print(sheet)
# print(ut.get_sheet_row(sheet))
# print(ut.get_sheet_col(sheet))
# print(ut.get_cell_value(sheet, 2, 4) == "自動")
# cfg = ut.get_conf_object("conf.ini")
# print(cfg)
# print(ut.get_section_option(cfg, "default", "key"))
new_wb = ut.create_excel_sheet()
new_sheet = ut.get_excel_sheet(new_wb, 0)
# # ut.write_sheet_cell(new_sheet, 1, 1, "test")
data = [1, 2, 3, 4, 5]
ut.write_sheet(new_sheet, data)
ut.fill_color(new_sheet, 1, 1, "FAIL")
ut.fill_color(new_sheet, 1, 2, "PASS")
ut.fill_color(new_sheet, 1, 3, "BLOCK")
new_sheet.cell(2, 3).value = "100"
ut.fill_color(new_sheet, 2, 3, "PASS")
# ut.write_sheet(new_sheet, data)
# A1 = new_sheet.cell(1, 1)
# A1.value = 100
# fill = PatternFill("solid", fgColor="1874CD")
ut.save_wb(new_wb, "test7.xlsx")
