Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
1
1
1
Traceback (most recent call last):
  File "/Users/geliang/Documents/a.py", line 7, in <module>
    print(str.format("本金利率和为{0:2.2f}",qw(a,b,n)))
  File "/Users/geliang/Documents/a.py", line 5, in qw
    amount=a*((1+b*0.01)**n)
TypeError: can't multiply sequence by non-int of type 'float'
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金12
本金利率和为12.00
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金0.333
本金利率和为0.33
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金44444444
本金利率和为44444444.00
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金12.846464684
本金利率和为12.85
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金0
本金利率和为0.00
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金1
本金利率和为1.00
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
请输入本金1.2
本金利率和为                                                                       1.20
>>> 
==================== RESTART: /Users/geliang/Documents/a.py ====================
输入4
共75位左空格补齐                                                                       4.00
>>> 
