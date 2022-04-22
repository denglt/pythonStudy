#!/usr/bin/python3

import redis

r = redis.Redis(host="127.0.0.1",port=36379,db=0,password="hsyt@redis")

r.set('foo', 'bar')

v = r.get('foo')  # byte3类型 python3新类型
print(v)
print(v.decode())

setV = (1,2,3)
r.sadd("my_set",*setV),

setV = r.smembers("my_set")

print(setV)  # set 类型


map = r.hgetall("HOSPITAL:CONFIG:HDP:ACCESS_TOKEN")  # dict 类型clea

print(len(map))


for key in map.keys():
    print(key, map[key])
