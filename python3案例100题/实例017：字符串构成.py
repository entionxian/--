# -*- coding: UTF-8 -*-
# 题目： 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析： 利用 while 或 for 语句,条件为输入的字符不为 ‘\n’。
string = input('输入字符串：')
spa = 0
num = 0
alp = 0
oth = 0
for i in range(len(string)):
    if string[i].isspace(): # 方法检测字符串是否只由空格组成,如果字符串中只包含空格，则返回 True，否则返回 False.
        spa+=1
    elif string[i].isdigit():
        num+=1
    elif string[i].isalpha():
        alp+=1
    else:
        oth+=1

print('space:',spa)
print('digit:',num)
print('alpha:',alp)
print('other:',oth)