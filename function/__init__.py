# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/7 11:22
import time


# a,b为形参
def calc(a, b):
    return a + b


# 1，4为实参
print(calc(1, 4))

print(calc(b=10, a=2))

"""
1 1 2 3 5 7 13 ...

if n ==1:
    return 1
if n > 1
    n = (n-1) + (n-2)


"""


def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


start1 = time.time()
# print(fibonacci_sequence(50))
print("fibonacci_sequence take second is ", str(time.time() - start1), "s")


def fibonacci_sequence1(n):
    if n == 1 or n == 2:
        return 1
    dic = dict()
    for i in range(1, n + 1):
        if i in dic:
            continue

        if i == 1 or i == 2:
            dic[i] = 1
        else:
            dic[i] = dic.get(i - 1) + dic.get(i - 2)
    return dic.get(n)

start2 = time.time()
print(fibonacci_sequence1(100))
print("fibonacci_sequence1 take second is ", str(time.time() - start2), "s")