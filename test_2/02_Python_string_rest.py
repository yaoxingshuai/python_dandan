# replace练习
string_1 = "let's do the replace!"
new_string = string_1.replace(' ', ',')
print(new_string)

# capitalize首字母大写练习
string_cap = "I want to use capitalize on this sentence"
print('#Output: (on each word):')
for word in string_cap.split():
    print(word.capitalize())

# 正则表达式练习
from math import exp, log, sqrt
import re

string_z = "This moment I am learning !this! zheng ze biao da shi"
string_list = string_z.split()
pattern = re.compile(r"This", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print(count)
