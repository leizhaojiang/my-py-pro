print("hello world")
# 打开文件，如果没有则新建文件
fp = open("data/test.txt", 'a+')

i = 0
while i < 100:
    # 将字符串输出到文件
    print("hello world", file=fp)
    i += 1

# 不换行输出
print("hello", "world")
# 换行符
print("hello\nworld")
# 空格符
print("hello\tworld")
# 覆盖
print("hello\rworld")
# 退一个字符 -> hellworld
print("hello\bworld")
fp.close()


