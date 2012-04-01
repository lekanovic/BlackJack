#!/usr/bin/python


class Gambler(object):
	def __init__(self,m):
		self.money = m
		self.bet = 0

	def place_bet(self,n):
		self.bet = n

	def won(self,m):
		self.money += m

	def lost(self,m):
		self.money -= m

class Player(object):
	def __init__(self,n):
		self.name = n
		self.hand = []

	def take_card(self,c):
		self.hand.append(c)

	def sum_hand(self):
		s=0
		for c in self.hand:
			s += c.value
		return s

	def throw_hand(self):
		self.hand = []
		self.place_bet = 0

	def add_house_card(self,c):
		self.house_card = c

	def more_cards(self):
		raise NotImplementedError("Subclass must implement")

	def cards_in_hand(self):
		return len(self.hand)

	def print_hand(self):
		v=[]
		for c in self.hand:
			v.append(str(c.value))
		print ','.join(v)

	def get_hand(self):
		v=[]
		for c in self.hand:
			v.append(str(c.value))
		return ','.join(v)

class Human(Player,Gambler):
	def __init__(self,n,m):
		Player.__init__(self,n)
		Gambler.__init__(self,m)

class Robot(Player,Gambler):
	def __init__(self,n,m):
		Player.__init__(self,n)
		Gambler.__init__(self,m)

	def more_cards(self):
		self.place_bet(1)
		if self.sum_hand() < 15:
			return True
		else:
			return False

class House(Player):
	def __init__(self,n):
		Player.__init__(self,n)

	def more_cards(self):
		if self.sum_hand() < 16:
			return True
		else:
			return False

class Smart(Player,Gambler):
	def __init__(self,n,m):
		Player.__init__(self,n)
		Gambler.__init__(self,m)

	def more_cards(self):
		card = self.house_card.value
		self.place_bet(1)
		if ((card == 5) or (card == 6)) and self.sum_hand() > 11:
			return False

		if self.sum_hand() >= 13 and self.sum_hand() <= 16 and card >= 2 and card <=6:
			return False

		if self.sum_hand() < 14:
			return True
		else:
			return False


def main():
	print "HEJ"

if __name__ == "__main__":
	main()
