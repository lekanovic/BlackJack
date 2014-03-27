#!/usr/bin/python
from random import randrange
from termcolor import colored
#Heart - u"\u2764"
#Diamond - u"\u2666"
#Spade - u"\u2660"
#Club - u"\u2663"


class Card:
	def __init__(self,v,c,t):
		if v == 11 or v == 12 or v == 13:
			self.value = 10
		else:
			self.value = v
		self.color = c
		self.card_type = t

class Deck:
	def __init__(self,n=1):
		self.cards = []

		for y in range(0,n):
			for x in range(1,53):
				value = (x%13)+1
				color = (x%2)
				card_type = (x%4)

				self.cards.append(Card(value,color,card_type))

	def print_cards(self):
		for a in self.cards:
			if ( a.card_type == 0):
				if ( a.color == 0 ): #Spade
					print colored(" %d" % (a.value),'red'),
					print colored(u"\u2660",'red')
				else:
					print colored(" %d" % (a.value),'grey'),
					print colored(u"\u2660",'grey')
			elif( a.card_type == 1):
				if ( a.color == 0 ): #Diamond
					print colored(" %d" % (a.value),'red'),
					print colored(u"\u2666",'red')
				else:
					print colored(" %d" % (a.value),'grey'),
					print colored(u"\u2666",'grey')
			elif( a.card_type == 2):
				if ( a.color == 0 ): #Heart
					print colored(" %d" % (a.value),'red'),
					print colored(u"\u2764",'red')
				else:
					print colored(" %d" % (a.value),'grey'),
					print colored(u"\u2764",'grey')
			elif( a.card_type == 3):
				if ( a.color == 0 ): #Club
					print colored(" %d" % (a.value),'red'),
					print colored( u"\u2663",'red')
				else:
					print colored(" %d" % (a.value),'grey'),
					print colored( u"\u2663",'grey')
			else:
				print "ERROR"

	#sattoloCycle
	def shuffle(self):
		for i in range(0,20):
			self.__knuth_shuffle()

	def __knuth_shuffle(self):
		i = len(self.cards)
		while i > 1:
			i = i - 1
			j = randrange(i)
			self.cards[j].value,self.cards[i].value = self.cards[i].value,self.cards[j].value

	def pop_card(self):
		return self.cards.pop()

	def cards_left(self):
		return len(self.cards)

def main():
	d1 = Deck()
#	d1.print_cards()
	d1.shuffle()
	d1.print_cards()
#	print d1.pop_card().value
#	print d1.pop_card().value
#	print d1.pop_card().value
#	print d1.cards_left()


if __name__ == "__main__":
	    main()
