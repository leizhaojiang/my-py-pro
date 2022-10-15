# 地点：西安
# 姓名：雷兆江
# 时间：2022/10/6 23:09

account = 20000
money = int(input("请输入取款金额"))
if money <= 20000:
    print("\n这是您的", str(money), "元")
    account = account - money
else:
    print("你的余额不足")
print('您的余额还有', account, '元')
