#!/usr/bin/python

from cards import Deck
from player import Robot
from player import House
from player import Smart
from statistic import Stats

import time

class Blackjack:
	def __init__(self,h,n=5):
		self.Stat = Stats()
		self.number_of_decks = n
		self.house = h
		self.players = []
		self.deck = Deck(self.number_of_decks)
		self.deck.shuffle()

	def throw_all_hands(self):
		for a in self.players:
			a.throw_hand()
		self.house.throw_hand()

	def add_player(self,p):
		self.players.append(p)

	def remove_player(self,p):
		[a for a in self.players if a.name == p]

	def play(self):
		print "*** Game started ***"
		#time.sleep(5)
		self.play_round()
		print "cards left %d" %	(self.deck.cards_left())

	def pop_card(self):
		#All cards are used create an new deck of cards
		if self.deck.cards_left() == 0:
			self.deck = Deck(self.number_of_decks)
			self.deck.shuffle()

		return self.deck.pop_card()

	def play_round(self):
		#First round players gets their cards
		for a in self.players:
			c = self.pop_card()
			a.take_card(c)

		#House gets the last card
		c = self.pop_card()
		self.house.take_card(c)

		#Let players know what card house got
		for a in self.players:
			a.add_house_card(c)

		#Now players can decide if they should
		#have more cards or stop
		for a in self.players:
			while a.more_cards():
				c = self.pop_card()
				a.take_card(c)

		#House turn to pick cards
		while self.house.more_cards():
			self.house.take_card( self.pop_card())

		sum = self.house.sum_hand()

		#Track all stats
		self.Stat.collect_data(self.house,self.players)

		#Round is over throw the cards holding
		self.throw_all_hands()

def main():
	game = Blackjack(House('Jimmy'))
	p1 = Robot("Calle")
	p2 = Robot("Nisse")
	p3 = Robot("Olle")
	p4 = Smart("Albert")

	game.add_player(p1)
	game.add_player(p2)
	game.add_player(p3)
	game.add_player(p4)

	for i in range(0,10):
		game.play()


if __name__ == "__main__":
	    main()
