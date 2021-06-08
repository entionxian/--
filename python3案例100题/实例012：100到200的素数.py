# -*- coding: UTF-8 -*-
# 题目 判断101-200之间有多少个素数，并输出所有素数。
# 程序分析 判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。 用else可以进一步简化代码
import math
sushu=[] # 素数列表
No = 0 # 素数的个数
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i))+1): #round() 方法返回浮点数x的四舍五入值。sqrt() 方法返回数字x的平方根。
        if i%j==0:
           break
    else:
        sushu.append(i)
        No+=1
print('一共有',No,'个素数')
print(sushu)


