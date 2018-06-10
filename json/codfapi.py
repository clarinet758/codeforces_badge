#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#not used

import time
import sys
import io
import re
import datetime
import json

n=''
filename="./data.json"

info='./info.json'
rating='./rating.json'
status='./status.json'
savedata="./data.json"

def jsonload(filename):
    f=open(filename)
    data=json.load(f)
    f.close()
    return data

data1=jsonload(info)
data2=jsonload(rating)
data3=jsonload(status)
master=jsonload(savedata)  


# can not get 'OK',do not update.  because do not know any time to recover.
if data1['status']!='OK': exit()
if data2['status']!='OK': exit()
if data3['status']!='OK': exit()

info=data1['result'][0]
cont=data2['result'][-1]
subm=data3['result'][0]

master['handle']=n
master['rankName']=info['rank']
master['maxRankName']=info['maxRank']
master['rating']=info['rating']
master['maxRating']=info['maxRating']
master['contestId']=str(cont['contestId'])
master['contestName']=cont['contestName']
master['contestRank']=cont['rank']
flu=cont['newRating']-cont['oldRating']
if flu>0:
    flu='+'+str(flu)
elif flu>=0:
    flu=str(flu)
master['fluctuation']=flu
master['fluctuation']=flu
dt=datetime.datetime.fromtimestamp(subm['creationTimeSeconds'])
if dt.month>9:
    mo=str(dt.month)
else:
    mo=('0'+str(dt.month))
if dt.day>9:
    dy=str(dt.day)
else:
    dy=('0'+str(dt.day))
if dt.hour>9:
    ho=str(dt.hour)
else:
    ho=('0'+str(dt.hour))
if dt.minute>9:
    mn=str(dt.minute)
else:
    mn=('0'+str(dt.minute))
if dt.second>9:
    sc=str(dt.second)
else:
    sc=('0'+str(dt.second))
ts=str(dt.year)+'-'+mo+'-'+dy+' '+ho+':'+mn+':'+sc
master['when']=ts
if subm['verdict']=='OK':
    subm['verdict']='Accepted'
master['verdict']=subm['verdict']
master['submitContestId']=str(subm['problem']['contestId'])
master['submitCodeId']=str(subm['id'])
master['index']=(subm['problem']['index'])
master['problemName']=(subm['problem']['name'])

json.dump(master, open(savedata, 'w'))
