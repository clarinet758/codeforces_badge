#!/usr/bin/env python3

import datetime
import urllib.request, urllib.error
import json

#0:テスト 1:本番 shellから受け取り
i = int(input())

#m = ["テスト", "本番"]
#print(m[i]+"で動作中")
#exit(1)


us = "clarinet758"
url   = "http://codeforces.com/api/user."
url_i = url + "info?handles=" + us
url_r = url + "rating?handle=" + us
url_s = url + "status?handle=" + us + "&from=1&count=1"

if i == 0:
    p  = "/home/reina/magic/cold/cf_badge/data.json"

elif i == 1:
    p  = "/var/www/html/joso/data.json"

else:
    exit(1)

f   = open(p)
mas = json.load(f)
f.close()
#print(mas)

def gj(url):
    res = urllib.request.urlopen(url)
    nama = res.read()
    nama8 = nama.decode("utf_8")
    j = json.loads(nama8)
    return j

def zero(s):
    if s//10:
        return str(s)
    else:
        return "0" + str(s)

error   = {"status": "ERROR"}
info    = gj(url_i)
rating  = gj(url_r)
status  = gj(url_s)

#3種のjsonがOKで用意できた場合には処理を続ける
if ("OK" == info["status"] == rating["status"] == status["status"]):
#if ("OK" == info["status"] == rating["status"] == status["status"] == error["status"]):
    #print("OK")
    pass
else:
    exit(1)

i = info["result"][0]
r = rating["result"][-1]
s = status["result"][0]

#コンテスト結果
mas["rankName"]    = i["rank"]
mas["maxRankName"] = i["maxRank"]
mas["rating"]      = i["rating"]
mas["maxRating"]   = i["maxRating"]
mas["contestId"]   = str(r["contestId"])
mas["contestName"] = r["contestName"]
mas["contestRank"] = r["rank"]
flu                = r["newRating"] - r["oldRating"]

if flu > 0:
    flu = "+"+str(flu)
else:
    flu = str(flu)
mas["fluctuation"] = flu

dt = datetime.datetime.fromtimestamp(s["creationTimeSeconds"])
mo = zero(dt.month)
dy = zero(dt.day)
ho = zero(dt.hour)
mn = zero(dt.minute)
sc = zero(dt.second)

ts = str(dt.year)+"-"+mo+"-"+dy+" "+ho+":"+mn+":"+sc
mas["when"] = ts

if s["verdict"] == "OK":
    s["verdict"] = "Accepted"
mas["verdict"]         = s["verdict"]
mas["submitContestId"] = str(s["problem"]["contestId"])
mas["submitCodeId"]    = str(s["id"])
mas["index"]           = str(s["problem"]["index"])
mas["problemName"]     = s["problem"]["name"]
#print(mas)

json.dump(mas, open(p, 'w'))
