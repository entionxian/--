# -*- coding: UTF-8 -*-
# 题目：求s=a+aa+aaa+aaaa+aa…a的值，
# 其中a是一个数字。例如2+22+222+2222+22222 (此时共有5个数相加)，几个数相加由键盘控制。
a = input('被加数字：')
n = input('加几次：')
res = 0
for i in range(int(n)):
    res+=int(a)
    a+=a[0] # 应该是在字符串a的所以0位置加上一个a的字符换
    print(a)
print('结果是：',res)