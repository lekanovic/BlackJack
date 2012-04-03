
class Stats:

	def pay_player(self,player):
		if self.has_blackjack(player):
			player.won(player.bet*2)
		else:
			player.won(player.bet)

	def has_blackjack(self,player):
		if player.cards_in_hand() == 2 and player.sum_hand() == 21:
			return True
		else:
			return False

	def collect_data(self,house,players):
		s = house.sum_hand()
		if s > 21:
			print "All player won house is BUST! %d=[%s]" % (s,house.get_hand())
			for a in players:
				if a.sum_hand() < 22:
					self.pay_player(a)
					self.print_data(a,"won");
				else:
					a.lost(a.bet)
					self.print_data(a,"lost-bust")
			return

		print "House %s has %d=[%s]" % (house.name,s,house.get_hand())
		for a in players:
			#if a.sum_hand() <= s and s < 22 or a.sum_hand() > 21:
			if a.sum_hand() <= s:
				a.lost(a.bet)
				self.print_data(a,"lost")
			elif a.sum_hand() < 22:
				self.pay_player(a)
				self.print_data(a,"won")
			else:
				a.lost(a.bet)
				self.print_data(a,"lost-bust")

	def print_data(self,a,outcome):
		if self.has_blackjack(a):
			print "%s %s!!. hand BlackJack %d=[%s] $%d bet $%d" %(a.name,outcome,a.sum_hand(),a.get_hand(),a.money,a.bet)
		else:
			print "%s %s!!. hand %d=[%s] $%d bet $%d" %(a.name,outcome,a.sum_hand(),a.get_hand(),a.money,a.bet)


