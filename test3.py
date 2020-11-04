# coding = utf-8
from utils import Utils as ut
values = ut.get_strings_flies_values("data/classic300s/iosl/en.lproj/Localizable.strings")
# print(values)
keys = ut.get_strings_key_by_vaule(values, "Take a Photo")
print(keys)
print(ut.get_strings_value_by_key(values, "VSTakePhoto"))