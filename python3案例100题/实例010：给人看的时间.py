# -*- coding: UTF-8 -*-
# 题目 暂停一秒输出，并格式化当前时间
import time 
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) # 注意括号的数量
    time.sleep(1)
