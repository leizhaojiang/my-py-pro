# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 10:05

scores = {'zhangsan': 100, 'lisi': 120, 'wangwu': 12}

print(scores.get('zhangsan'))
print(scores['zhangsan'])

print('zhangsan' in scores)
print('zhangsan' not in scores)

del scores['zhangsan']
print(scores)

scores['chenliu'] = 19
print(scores)

keys = scores.keys()
print(list(keys))
values = list(scores.values())
print(values)
items = list(scores.items())
print(items)
print('========================')
for item in scores.items():
    print(item)
for key in scores.keys():
    print(scores.get(key))
