#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import datetime
import urllib2
import json

n=''
endpoint1='http://codeforces.com/api/user.info?handles='+n
endpoint2='http://codeforces.com/api/user.rating?handle='+n
endpoint3='http://codeforces.com/api/user.status?handle='+n+'&from=1&count=1'
filename="./data.json"
d=urllib2.urlopen(endpoint1)
data1=json.load(d)
d.close()
d=urllib2.urlopen(endpoint2)
data2=json.load(d)
d.close()
d=urllib2.urlopen(endpoint3)
data3=json.load(d)
d.close()
f=open(filename)
master=json.load(f)
f.close()
# can not get 'OK',do not update.  because do not know any time to recover.
if data1[u'status']!='OK': exit()
if data2[u'status']!='OK': exit()
if data3[u'status']!='OK': exit()

info=data1[u'result'][0]
cont=data2[u'result'][-1]
subm=data3[u'result'][0]

master[u'handle']=n
master[u'rankName']=info['rank']
master[u'maxRankName']=info['maxRank']
master[u'rating']=info['rating']
master[u'maxRating']=info['maxRating']
master[u'contestId']=str(cont['contestId'])
master[u'contestName']=cont['contestName']
master[u'contestRank']=cont['rank']
flu=cont['newRating']-cont['oldRating']
if flu>0:
    flu='+'+str(flu)
elif flu>=0:
    flu=str(flu)
master[u'fluctuation']=flu
master[u'fluctuation']=flu
dt=datetime.datetime.fromtimestamp(subm[u'creationTimeSeconds'])
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
master[u'when']=ts
if subm[u'verdict']==u'OK':
    subm[u'verdict']=u'Accepted'
master[u'verdict']=subm[u'verdict']
master[u'submitContestId']=str(subm[u'problem'][u'contestId'])
master[u'submitCodeId']=str(subm[u'id'])
master[u'index']=(subm[u'problem'][u'index'])
master[u'problemName']=(subm[u'problem'][u'name'])

json.dump(master, open(filename, 'w'))
