#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))


dd = dict( name = 'denglt', age = 19)

print(dd.get('name'))
print(dd.get('age'))

dd.update(name='zyy',address='guangzhou')
print(dd)

print(dd.items().__class__)

keys = dd.keys()
print('keys =' , keys)

print(keys is list)
print(keys.__class__)
print(isinstance(keys,list))

for key in keys:
    print(key)

print('name' in dd)  # is true 

for key in dd: # like dd.keys()
    print(key)