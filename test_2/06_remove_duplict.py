import pandas as pd
import numpy as np

# 加载路径
path_csv = '/home/yaoxing/task_0330/task_1_remove_duplicate_number.csv'
path_excel = '/home/yaoxing/task_0330/task_1_remove_duplicate_number.xlsx'
path_txt = '/home/yaoxing/task_0330/task_1_remove_duplicate_number.txt'

# 读取文件
file_csv = pd.read_csv(path_csv, header=None, usecols=[0, 1])
file_excel = pd.read_excel(path_excel, header=None, usecols=[0, 1])
file_txt = pd.read_table(path_txt, header=None, usecols=[0, 1])

# 使用array变为list
np_csv = np.array(file_csv)
np_excle = np.array(file_excel)

# 去重操作
l1 = []
s1 = set()

for i in np_csv:
    if i[0] in s1:
        pass
    else:
        l1.append(i)
        s1.add(i[0])

# 导出文件为csv格式
name = ['data', 'num']
li_df = pd.DataFrame(data=l1, columns=name, index=None)
li_df.to_csv('/home/yaoxing/task_0330/task_1_result.csv', encoding='utf-8', index=False)
