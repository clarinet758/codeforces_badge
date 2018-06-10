#!/bin/sh

# 0:テスト用 1:本番用
type_code=1
if [ ${type_code} -eq 0 ]
    then
    lo="xxx"
    jh=${lo}
elif [ ${type_code} -eq 1 ]
    then
    lo="xxx"
    jh="ooo"
fi

#ベースになるjson作成、作成失敗してればshellも終了させる
py="${lo}cf_badge.py"
echo ${type_code} | ${py}

#echo $?
if [ $? -ne 0 ]
  then
  exit 1
fi

#pyで作成したjsonを無理やりjsonpにする
echo 'parseResponse(' > ${jh}data.jsonp
cat ${jh}data.json >> ${jh}data.jsonp
echo ');' >> ${jh}data.jsonp
exit 0
