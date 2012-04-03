#!/usr/bin/python

from cards import Deck
from player import Robot
from player import House
from player import Smart
from player import Genious
from player import Human

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
			a.clear_bet()
		self.house.throw_hand()

	def add_player(self,p):
		self.players.append(p)

	def remove_player(self,p):
		[a for a in self.players if a.name == p]

	def play(self,silent=False):
		print "*** Game started ***"
		self.play_round(silent)
		print "cards left %d" %	(self.deck.cards_left())
		print "*** Game End ***\n"

	def pop_card(self):
		#All cards are used create an new deck of cards
		if self.deck.cards_left() == 0:
			self.deck = Deck(self.number_of_decks)
			self.deck.shuffle()

		return self.deck.pop_card()

	def start_deal(self,silent):
		#Has all player money left
		for a in self.players:
			if a.money <= 0:
				print "%s lost all money" % (a.name)
				exit(1)

		#Players gets their first cards
		for a in self.players:
			c = self.pop_card()
			a.place_bet(1)
			a.take_card(c)
			if not silent:
				print "%s hand %d=[%s]" % (a.name,a.sum_hand(),a.get_hand())

		#House gets it's first card
		c = self.pop_card()
		self.house.take_card(c)
		if not silent:
			print "House hand %d" % (c.value)

		#Let players know what card house got
		for a in self.players:
			a.add_house_card(c)

		#Players gets their second cards
		for a in self.players:
			c = self.pop_card()
			a.take_card(c)
			if not silent:
				print "%s hand %d=[%s]" % (a.name,a.sum_hand(),a.get_hand())

		#House gets it's second card but is not
		#showed to players.
		c = self.pop_card()
		self.house.take_card(c)


	def play_round(self,silent):

		self.start_deal(silent)

		#Now players can decide if they should
		#have more cards or stop
		for a in self.players:
			while a.more_cards():
				c = self.pop_card()
				a.take_card(c)
				if not silent:
					print "%s hand %d=[%s]" % (a.name,a.sum_hand(),a.get_hand())

		#House turn to pick cards
		while self.house.more_cards():
			self.house.take_card( self.pop_card())

		#Track all stats
		self.Stat.collect_data(self.house,self.players)

		#Round is over throw the cards holding
		#and clear all bets.
		self.throw_all_hands()

	def show_results(self):
		print "not implemented yet"

def main():
	cash = 100
	game = Blackjack(House('Jimmy'))
	p1 = Robot("Calle",cash)
	p2 = Robot("Nisse",cash)
	p3 = Robot("Olle",cash)
	p4 = Smart("Albert",cash)
	p5 = Genious("Radovan",cash)
	#p6 = Human("Sulka",cash)

	#game.add_player(p6)
	game.add_player(p5)
	game.add_player(p2)
	game.add_player(p3)
	game.add_player(p4)
	game.add_player(p1)

	while True:
		game.play(silent=True)

	game.show_results()

if __name__ == "__main__":
	    main()
