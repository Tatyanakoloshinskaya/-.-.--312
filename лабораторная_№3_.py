# -*- coding: utf-8 -*-
"""Лабораторная №3.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZO9YrCAG_tqbu0wJdXhwHQS8DupJuW8E
"""

x=int(input())
if x==1: print("январь")
elif x==2: print("февраль")
elif x==3: print("март")
elif x==4: print("апрель")
elif x==5: print("май")
elif x==6: print("июнь")
elif x==7: print("июль")
elif x==8: print("август")
elif x==9: print("сентябрь")
elif x==10: print("октябрь")
elif x==11: print("ноябрь")
elif x==12: print("декабрь")

x=int(input())
if x%2==0: print("чётное")
elif x%2!=0: print("нечётное")

N=int(input())
if N>40: print("stonks")
elif N<40: print("not stonks")

is_year_leap=int(input())
if is_year_leap%4==0: print("true")
elif is_year_leap%4!=0: print("false")

from sympy import *
isprime(5)

a = float(input())
b = float(input())

if (a / b==3.6) or ((-138 / 2) ** 1.3 <= b <=-69 / 28 ** 5.1* 4):
 a, b = b, a
print(a, b)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a!=b!=c!=d!=e: print("все уникальные")
else: print("не все уникальные")
if a%2==0 and b%2==0 and c%2==0 and d%2==0 and e%2==0: print("все чётные")
else: print("не все чётные")

"""Задание повышенной сложности:"""

a=int(input()) 
b=int(input()) 
c=int(input()) 
z=(((a**2)+(b**3))/(c+3))/4
if z%2==0: print("чётное")
elif z%2!=0: print("нечётное")