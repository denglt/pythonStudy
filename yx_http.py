#!/usr/bin/python3
import requests

requestData = {"accid": "sysmanager"}
requestHeader = {
    'appkey': '78e60bb2f3674216f052c93ff35b9898',
    'checksum': 'd567b94a112dedcbfe93fb4d225ad5aab25d5b94',
    'content-type': 'application/x-www-form-urlencoded',
    'curtime': '1486718966',
    'nonce': '123456'
}
r = requests.post("https://api.netease.im/nimserver/team/joinTeams.action",
                  data=requestData, headers=requestHeader)
print(r.request.headers)
print(r.status_code)
print(r.headers)
print(r.cookies)
data = r.json()

if (data["count"]>0):
    tids = list(map(lambda qz: qz["tid"], data["infos"]))
    print(len(tids))
    rmQzUrl = "https://api.netease.im/nimserver/team/remove.action"

    for tid in tids:
        requestData ={"owner":"sysmanager"}
        requestData["tid"]=tid
        print(tid)
        # 注释掉防止误删除 
        # requests.post(rmQzUrl,data=requestData,headers=requestHeader)

# https://requests.readthedocs.io/en/latest/user/advanced/   高级功能
# requests 高级功能 session
'''
     The Session object allows you to persist certain parameters across requests. 
     It also persists cookies across all requests made from the Session instance, and will use urllib3’s connection pooling.
     So if you’re making several requests to the same host, the underlying TCP connection will be reused, 
     which can result in a significant performance increase (see HTTP persistent connection).
'''