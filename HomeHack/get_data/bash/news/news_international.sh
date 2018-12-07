#!/bin/sh
# file name: news_international.sh
wget -q -O - https://www3.nhk.or.jp/rss/news/cat6.xml|grep -e "<title>[^<]*</title>" -e "<description>[^<]*</description>" -e "<pubDate>[^<]*</pubDate>" | sed -e 's:<title>::g' -e 's:</title>::g' -e 's:<description>::g' -e 's:</description>::g' -e 's:,::g' -e 's:<pubDate>::g' -e 's:</pubDate>::g' -e 's:+0900::g' -e 's:Mon:月曜:g' -e 's:Tue火曜::g' -e 's:Wed:水曜:g' -e 's:Thu:木曜:g' -e 's:Fri:金曜:g' -e 's:Sat:土曜:g' -e 's:Sun:日曜:g' -e 's:Jan:1月:g' -e 's:Feb:2月:g' -e 's:Mar:3月:g' -e 's:Apr:4月:g' -e 's:May:5月:g' -e 's:Jun:6月:g' -e 's:Jul:7月:g' -e 's:Aug:8月:g' -e 's:Sep:9月:g' -e 's:Oct:10月:g' -e 's:Nov:11月:g' -e 's:Dec:12月:g' > ./get_data/news_get.txt
exit 0
