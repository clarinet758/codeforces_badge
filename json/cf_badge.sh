#!/bin/sh
wget -q -t 5 -O ./info.json -N http://codeforces.com/api/user.info?handles=****
wget -q -t 5 -O ./rating.json -N http://codeforces.com/api/user.rating?handle=****
wget -q -t 5 -O ./status.json -N http://codeforces.com/api/user.status?handle=****&from=1&count=1
./codefapi.py
echo 'parseResponse(' > ./data.jsonp
cat ./data.json >> ./data.jsonp
echo ');' >> ./data.jsonp
