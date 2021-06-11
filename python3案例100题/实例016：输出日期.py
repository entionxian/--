# -*- coding: UTF-8 -*-
# 题目 输出指定格式的日期。使用 datetime 模块。
import datetime
print(datetime.date.today()) # 获取当前日期
print(datetime.date(2333,2,3)) # 打印指定的日期
print(datetime.date.today().strftime('%d/%m/%Y')) # 以固定格式显示当前日期
day=datetime.date(1111,2,3) # 生成指定的日期
day=day.replace(year=day.year+22) # 将上述生成日期中的年份+22后，替换成新值
print(day)