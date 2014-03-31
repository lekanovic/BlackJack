#!/bin/bash


#-------------------
rm log 2>&1
rm most_money 2>&1
echo 1 > gofile

times_lost_albert=0
times_lost_radovan=0
times_lost_olle=0
times_lost_calle=0
times_lost_nisse=0
most_money=0

printf "\r\n"
rounds_played=0

while [ 1 ]
do
	((rounds_played++))
	python blackjack.py > log

	who_lost=$(cat log|grep "lost all money"|tail -1)
	if  [[ $who_lost == Radovan* ]]; then
		((times_lost_radovan++))
	elif  [[ $who_lost == Olle* ]]; then
		((times_lost_olle++))
	elif  [[ $who_lost == Nisse* ]]; then
		((times_lost_nisse++))
	elif  [[ $who_lost == Calle* ]]; then
		((times_lost_calle++))
	elif  [[ $who_lost == Albert* ]]; then
		((times_lost_albert++))
	fi

	money=$(cat log|egrep "hand|hand BlackJack"|awk 'NF ''{print $(NF-2)}'|sed -e 's/\$//g'|uniq |sort -n|tail -1)

	if [ $money -gt $most_money ]; then
		most_money=$money
		printf " Most money $%d %s\n" $most_money $(cat log|grep "\$$most_money"|tail -1|awk '{print $1}') >> most_money
	fi

	printf " Nisse lost %d " $times_lost_nisse
	printf " Radovan lost %d " $times_lost_radovan
	printf " Olle lost %d " $times_lost_olle
	printf " Albert lost %d " $times_lost_albert
	printf " Calle lost %d " $times_lost_calle
	printf " Rounds played %d \r" $rounds_played

	if [ $(cat gofile) == 0 ]; then
		printf "\r\n"
		exit
	fi

done

echo "\r\n"
echo "Nisse lost " $(cat log|grep "lost all"|grep Nisse|wc -l)
echo "Radovan lost " $(cat log|grep "lost all"|grep Radovan|wc -l)
echo "Olle lost " $(cat log|grep "lost all"|grep Olle|wc -l)
echo "Calle lost " $(cat log|grep "lost all"|grep Calle|wc -l)
echo "Albert lost " $(cat log|grep "lost all"|grep Albert|wc -l)



