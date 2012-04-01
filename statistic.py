


class Stats:
	def __init__(self):
		print "stat"

	def collect_data(self,house,players):
		s = house.sum_hand()
		if s > 21:
			print "All player won house is TJOCK!"
			for a in players:
				if a.sum_hand() < 22:
					print "%s won!!. hand %d" % (a.name,a.sum_hand())
					a.print_hand()
			return

		print "House %s has %d in his hand" %(house.name,s)
		for a in players:
			if a.sum_hand() <= s and s < 22 or a.sum_hand() > 21:
				print "%s lost!!. hand %d" % (a.name,a.sum_hand())
			else:
				print "%s won!!. hand %d" % (a.name,a.sum_hand())
			a.print_hand()

