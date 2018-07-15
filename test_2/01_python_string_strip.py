# 测试pandas是否安装成功
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

records = [{'name': 'dan', 'age': 18}, {'name': 'star', 'age': 20}, {'name': 'rui', 'age': 20}]
frame = DataFrame(records)
print(frame)

# strip函数练习，去除两端的空格或者字符
string1 = "___Remove unwanted   from this string. \t\t    \n +++$$$"
print("Output#1: string1: {}".format(string1))

string1_lstrip = string1.lstrip()
print("Output#2: lstrip: {}".format(string1_lstrip))

string1_rstrip = string1.rstrip()
print("Output#3: rstrip: {}".format(string1_rstrip))

string1_strip = string1.strip('_+$')
print("Output#4: strip: {}".format(string1_strip))
