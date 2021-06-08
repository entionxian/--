# -*- coding: UTF-8 -*-
# 题目 将一个整数分解质因数。每个合数都可以写成几个质数相乘的形式，其中每个质数都是这个合数的因数，
# 把一个合数用质因数相乘的形式表示出来，叫做分解质因数
# 程序分析 根本不需要判断是否是质数（素数），从2开始向数本身遍历，能整除的肯定是最小的质数。

target = int(input('输入一个整数：'))
print(target,'= ',end='')

if target<0:
    target=abs(target)
    print('-1*',end='')

flag = 0
if target<=1:
    print(target)
    flag = 1

while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i == 0:
            print('%d'%i,end='')
            if target == i:
                flag =1
                break
            print('*',end='')
            target/=i # 除法赋值运算符,c /= a 等效于 c = c / a
            break