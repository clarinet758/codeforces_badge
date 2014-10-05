#!/bin/sh
./codefapi.py
echo 'parseResponse(' > ./data.jsonp
cat ./data.json >> ./data.jsonp
echo ');' >> ./data.jsonp
