#!/usr/bin/env python3
# coding:utf-8

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)
print(classmates is list)
print(isinstance(classmates,list))
print(classmates.__class__)



age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager');