import difflib

text1 = "Turn on your phone\'s  Bluetooth, so VeSync can connect to your device."
text2 = "Turn on your phone\'s  Bluetooth, so Vesync can connect to your device."
text1_lines = text1.splitlines(keepends=True)  # 分别以行进行分割
text2_lines = text2.splitlines(keepends=True)

# d = difflib.Differ()                # 创建Differ对象
# diff = d.compare(text1_lines, text2_lines)
# print('\n'.join(list(diff)))

d = difflib.Differ()
result = d.compare(text1_lines, text2_lines)
print("\n".join(list(result)))
