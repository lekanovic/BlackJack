
class Stats:

	def collect_data(self,house,players):
		s = house.sum_hand()
		if s > 21:
			print "All player won house is TJOCK! %d=[%s]" % (s,house.get_hand())
			for a in players:
				if a.sum_hand() < 22:
					self.print_data(a,"won");
				else:
					self.print_data(a,"lost-tjock")
			return

		print "House %s has %d=[%s]" % (house.name,s,house.get_hand())
		for a in players:
			if a.sum_hand() <= s and s < 22 or a.sum_hand() > 21:
				if a.sum_hand() > 21:
					self.print_data(a,"lost-tjock")
				else:
					self.print_data(a,"lost")
			else:
				self.print_data(a,"won")

	def print_data(self,a,outcome):
		print "%s %s!!. hand %d=[%s]" % (a.name,outcome,a.sum_hand(),a.get_hand())

