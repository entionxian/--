# -*- coding: UTF-8 -*-
# 题目 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析 利用for循环控制100-999个数，每个数分解出个位，十位，百位。
# 一共有 4 个水仙花数 [153, 370, 371, 407]

#方法1：索引所有的三位数，通过拆分出个位十位百位
ShuiXianHua = []
No = 0
for i in range(100,1000):
    s = str(i)
    one = int(s[-1])
    ten = int(s[-2])
    hun = int(s[-3])
    if i == one**3+ten**3+hun**3:
        No+=1
        ShuiXianHua.append(i)
print('一共有',No,'个水仙花数:',ShuiXianHua)

# 方法2：分别索引个，十，百
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j**3+k**3 == int(str(i)+str(j)+str(k)):
                print(int(str(i)+str(j)+str(k)))