#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny   # 返回多个值 ，实际上返回的是一个tuple对象


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
# my_abs('123')

# 空函数


def nop():
    pass


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Adam', 'M', city='Tianjin')

enroll(city='Tianjin', name='Adam', gender='M')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数


def calc(numbers):  # 作为一个list或tuple传进来
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc([1, 2, 3])
calc((1, 3, 5, 7))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc2(1, 2, 3)

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
calc2(*nums)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):  # kw 是一个dict
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)

person('Bob', 35, city='Beijing', address='guangzhou', address2='asfasdf')


def person(name, age, *, city, job):  # *后面的参数被视为命名关键字参数
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):  # 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
    print(name, age, args, city, job)


person('Jack', 24, city='Beijing', job='Engineer')

# 参数组合


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')  # a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)  # a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)  # a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
