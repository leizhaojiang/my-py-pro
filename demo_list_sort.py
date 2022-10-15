# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 09:44

lst = [12, 3, 43, 7, 45, 34, 12]

# lst.sort()

new_list = sorted(lst)
new_list.reverse()

print("原列表：", str(lst))
print("新列表：", str(new_list))

desc_list = [i**2 for i in range(0, 11)]

print(desc_list)