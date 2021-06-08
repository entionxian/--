# -*- coding: UTF-8 -*-
# 斐波那契数列（Fibonacci sequence）
# 从1,1开始，后面每一项等于前面两项之和。
#方法1：递归实现
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
    
print(Fib(int(input())))
  

#方法2：循环实现，性能更好
target=int(input())
res=[1]
a,b =1,1
for i in range(target-1):
    a,b=b,a+b
    res.append(a)
print(res)