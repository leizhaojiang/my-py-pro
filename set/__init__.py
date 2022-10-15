# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 10:49

s1 = {1, 2, 3, 4}
s1.add(5)
s1.pop()
for i in s1:
    print(i)
s2 = {12, 34, 56}
s3 = {40, 12, 34}

print(s2.issuperset(s3))
print(s2.issubset(s3))
print(s2.isdisjoint(s3))
print(s2 - s3)

help(print)