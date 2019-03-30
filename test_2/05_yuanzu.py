s1 = ('yx', 6)
s2 = ('cd', 7)
s3 = ('cd', 3)
s4 = ('yx', 4)
s5 = ('cd', 5)

li = [s1, s2, s3, s4, s5]

# 对名字有序去重
s3 = set()
li3 = []
for i in li:
    if i[0] in s3:
        pass
    else:
        li3.append(i[0])
        s3.add(i[0])
print(li3)

# 取出每个名字对应最大的编号

dic = dict()
for i in li:
    if i[0] not in dic:
        dic[i[0]] = i[1]
    else:
        if dic[i[0]] < i[1]:
            dic[i[0]] = i[1]
        else:
            pass
print(dic)

li4 = []
for i in li3:
    li4.append((i, dic[i]))
print(li4)


