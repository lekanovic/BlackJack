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

	def clear_bet(self):
		self.bet = 0

class Player(object):
	def __init__(self,n):
		self.name = n
		self.hand = []

	def take_card(self,c):
		self.hand.append(c)

	def sum_hand(self):
		soft = self.sum_hand_soft()
		hard = self.sum_hand_hard()

		if hard > 21:
			return soft
		else:
			return hard

	#Soft hand means ace == 11
	def sum_hand_soft(self):
		s=0
		for c in self.hand:
			s += c.value
		return s

	#Hard hand means ace == 1
	def sum_hand_hard(self):
		s=0
		for c in self.hand:
			if c.value == 1:
				s += 11
				continue
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
		if self.sum_hand() < 15:
			return True
		else:
			return False

class House(Player):
	def __init__(self,n):
		Player.__init__(self,n)

	def more_cards(self):
		hand = self.sum_hand()
		if hand <= 16:
			return True
		elif hand >= 17 and hand <= 18:
			return False
		else:
			return False

class Smart(Player,Gambler):
	def __init__(self,n,m):
		Player.__init__(self,n)
		Gambler.__init__(self,m)

	def more_cards(self):
		card = self.house_card.value
		hand = self.sum_hand()

		if ((card == 5) or (card == 6)) and hand > 11:
			return False

		if hand >= 13 and hand <= 16 and card >= 2 and card <=6:
			return False

		if hand < 14:
			return True
		else:
			return False

#Genious player is using tactics described on:
#http://casinogambling.about.com/library/blbjmstrat.htm
class Genious(Player,Gambler):
	def __init__(self,n,m):
		Player.__init__(self,n)
		Gambler.__init__(self,m)

	def try_soft_hand(self):
		card = self.house_card.value
		mysum = self.sum_hand_soft()
		if mysum >= 3 and mysum <=4 and card >= 2 and card <= 4:
			return True
		if mysum >= 3 and mysum <= 4 and card >= 5 and card <= 6:
			self.place_bet(2*self.bet)
			return True
		if mysum >= 3 and mysum <= 4 and card >= 7:
			return True
		if mysum >= 5 and mysum <= 6 and card >= 2 and card <= 3:
			return True
		if mysum >= 5 and mysum <= 6 and card >= 4 and card <= 6:
			self.place_bet(2*self.bet)
			return True
		if mysum >= 5 and mysum <=6 and card >= 7:
			return True
		if mysum == 7 and card == 2:
			return True
		if mysum == 7 and card >= 3 and card <= 6:
			self.place_bet(2*self.bet)
			return True
		if mysum == 7 and card >= 7 and card <= 8:
			return False
		if mysum == 7 and card >= 9:
			return True
		if mysum == 8 and card == 2:
			return False
		if mysum >= 9 and mysum <= 10:
			return False


	def try_hard_hand(self):
		card = self.house_card.value
		if card == 1:
			card == 11

		mysum = self.sum_hand_hard()
		if mysum <= 8:
			return True
		if mysum == 9 and card == 2:
			return True
		if mysum == 9 and card >= 3 and card <= 6:
			self.place_bet(2*self.bet)
			return True
		if mysum  == 9 and card >= 7:
			return True
		if mysum == 10 and card >=2 and card <= 9:
			self.place_bet(2*self.bet)
			return True
		if mysum == 10 and card > 9:
			return True
		if mysum == 11 and card >= 2 and card <= 10:
			self.place_bet(2*self.bet)
			return True
		if mysum == 11 and card == 11:
			return True
		if mysum == 12 and card >= 2 and card <= 3:
			return True
		if mysum == 12 and card >= 4 and card <= 6:
			return False
		if mysum == 12 and card >= 7:
			return True
		if mysum >= 13 and mysum <= 16 and card <= 6:
			return False
		if mysum >= 13 and mysum <= 16 and card >= 7:
			return True
		return False

	def more_cards(self):
		soft = self.sum_hand_soft()
		hard = self.sum_hand_hard()
		print "soft %d hard %d " % (soft,hard)
		if soft == hard:
			return self.try_hard_hand()
		else:
			return self.try_soft_hand()

from cards import Card
def main():
	p1 = Genious("Radde",100)
	c = []
	c.append(Card(5,1,1))
	c.append(Card(3,1,1))
	c.append(Card(1,1,1))
	c.append(Card(6,1,1))
	c.append(Card(1,1,1))
	c.append(Card(10,1,1))

	p1.place_bet(1)
	p1.add_house_card(Card(9,1,1))

	while True:
		print "bet=%d money=%d hand %d=[%s]" % (p1.bet,p1.money,p1.sum_hand(),p1.get_hand())
		if p1.more_cards():
			print "more cards"
		else:
			break
		p1.take_card(c.pop())

	p1.won(p1.bet)
	print "bet=%d money=%d hand %d=[%s]" % (p1.bet,p1.money,p1.sum_hand(),p1.get_hand())

if __name__ == "__main__":
	main()
