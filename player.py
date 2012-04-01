#!/usr/bin/python


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

	def add_house_card(self,c):
		self.house_card = c

	def more_cards(self):
		raise NotImplementedError("Subclass must implement")

	def cards_in_hand(self):
		return len(self.hand)

	def print_hand(self):
		v=[]
		for c in self.hand:
			v.append(c.value)
		print v

class Human(Player):
	def __init__(self,n):
		Player.__init__(self,n)

class Robot(Player):
	def __init__(self,n):
		Player.__init__(self,n)

	def more_cards(self):
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

class Smart(Player):
	def __init__(self,n):
		Player.__init__(self,n)

	def more_cards(self):
		card = self.house_card.value
	#	print "value %d cards in hand %d" % (card,self.cards_in_hand())
		if ((card == 5) or (card == 6)) and self.sum_hand() > 11:
			return False

		if self.sum_hand() < 15:
			return True
		else:
			return False


def main():
	print "HEJ"

if __name__ == "__main__":
	main()
