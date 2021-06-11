# -*- coding: UTF-8 -*-
# 题目 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示。
#方法1：
points=int(input('输入分数：'))
if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade ='B'
print(grade)

#方案2：
def grade(x):
    if x>=90:
        return 'A'
    elif x<60:
        return 'C'
    else:
        return 'B'

points2=int(input('输入分数：'))
grade2=grade(points2)
print(grade2)

