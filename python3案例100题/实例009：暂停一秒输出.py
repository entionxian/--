# -*- coding: UTF-8 -*-
# 题目 暂停一秒输出,程序分析 使用 time 模块的 sleep() 函数。
import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)


# python中[-1]、[:-1]、[::-1]、[2::-1]的使用方法
a=[1,2,3,4,5,6,7,8,9]
print(a)
print(a[-2:]) # 从后往前2个元素
print(a[-1]) # 最后一个元素
print(a[:-1]) # 除了最后一个取全部
print(a[::-1]) # 取从后往前的元素
print(a[2::-1]) # 取索引为2元素反转读取