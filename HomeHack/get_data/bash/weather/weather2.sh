#!/bin/sh
# file name: weather.sh
#[^<]:<以外の文字
#*:直前の文字（[]内も１文字とする）の０回以上の繰り返し
#[^<]*:”<以外の文字”の０回以上の繰り返し
#^:行頭　\s*:０回以上の繰り返しの空白 $:行末
wget -q -O - http://www.jma.go.jp/jp/week/314.html | grep -e '<caption style="text-align:left;">[^<]*</caption>' -e '<td class="for" nowrap>[^<]*<br>' -e '<th class="[^/]*/th>' -e '<td class="for">[^d]*d>' -e '<td class="for" nowrap>[^b]*br>' | sed -e 's/<caption style[^>]*>//g' -e 's:</caption>::g' -e 's:	::g' -e 's:<br>::g' -e 's:</th>::g' -e 's:</td>::g' -e 's:</font>::g' -e 's/<th class=[^>]*>//g' -e 's/<td class=[^>]*>//g' -e 's/<font class=[^>]*>//g' -e 's:<img src="img/:\n./png/:g' -e 's/"[^>]*>//g' | sed '/^\s*$/d' > ./get_data/weather_get.txt
#grep -v '^\s*$' get.txt > fin.txt
exit 0
