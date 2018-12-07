#!/bin/sh
# file name: weather.sh
wget -q -O - https://www.drk7.jp/weather/xml/08.xml > test.xml
#[^<]:<以外の文字
#*:直前の文字（[]内も１文字とする）の０回以上の繰り返し
#[^<]*:”<以外の文字”の０回以上の繰り返し
grep -e "<author>[^<]*</author>" -e "<pubDate>[^<]*</pubDate>" -e "<pref id[^>]*>" -e "<area id[^>]*>" -e "<info date[^>]*>" -e "<weather>[^<]*</weather>" -e "<img>[^<]*</img>" -e "<weather_detail>[^<]*</weather_detail>" -e "<range centigrade=[^>]*>[^<]*</range>" -e "<period hour=[^>]*>[^<]*</period>" test.xml |sed  -e 's:<author>::g' -e 's:</author>::g' -e 's:<weather>::g' -e 's:</weather>::g' -e 's:<weather_detail>::g' -e 's:</weather_detail>::g' -e 's:</range>::g' -e 's:</period>::g' -e 's:<img>::g' -e 's:</img>::g' -e 's:<pref id="::g' -e 's:<area id="::g' -e 's:<info date="::g' -e 's:<range::g' -e 's:centigrade="::g' -e 's:max::g' -e 's:min::g' -e 's:<period::g' -e 's:hour="::g' -e 's:00-06::g' -e 's:06-12::g' -e 's:12-18::g' -e 's:18-24::g' -e 's:">::g' -e 's: ::g' -e 's:　::g'  > test.txt
exit 0
