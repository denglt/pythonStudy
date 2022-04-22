#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(*args, **kw):  # *args 可变参数   **kw 关键字参数
    print('args =', args, 'kw =', kw)


args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}

f(args)  # args = ((1, 2, 3),) kw = {}
f(args, kw)  # args = ((1, 2, 3), {'d': 88, 'x': '#'}) kw = {}
f(args, *kw)  # args = ((1, 2, 3), 'd', 'x') kw = {}
f(args, **kw)  # args = ((1, 2, 3),) kw = {'d': 88, 'x': '#'}

f(*args)  # args = (1, 2, 3) kw = {}
f(*args, kw)  # args = (1, 2, 3, {'d': 88, 'x': '#'}) kw = {}
f(*args, *kw)  # args = (1, 2, 3, 'd', 'x') kw = {}
f(*args, **kw)  # args = (1, 2, 3) kw = {'d': 88, 'x': '#'}

f(kw)  # args = ({'d': 88, 'x': '#'},) kw = {}
f(*kw)  # args = ('d', 'x') kw = {}
f(**kw)  # args = () kw = {'d': 88, 'x': '#'}
