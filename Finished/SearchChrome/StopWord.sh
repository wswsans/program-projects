#!/bin/bash
echo -n '閉じる単語: '
read stopStr


while true ; do
	tabs=`chrome-cli list links`
	declare -a tabls=();
	tabls=${tabs//\n/ };
	for dir in ${tabls[@]}; do
		if [[ $dir == *\[* ]]; then
			tabid=${dir:1}
			tabid=${tabid##*\:}
			tabid=${tabid:0:4}
		fi
 		if [[ $dir == *youtube* ]]; then
 			echo -n 'FOUND: '
 			echo $tabid
 			chrome-cli close -t $tabid
 		fi
	done
done
