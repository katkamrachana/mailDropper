import random
import sys

class Clearance(object):
	"""docstring for Clearance"""
	def __init__(self):
		super(Clearance, self).__init__()
		self.in_queue = None
		
	def input_values(self):
		try:
			self.total_flights = int(raw_input("Enter Flights count\t: "))
			self.total_freights = int(raw_input("Enter Freights count\t: "))
		except ValueError as verr:
			print "Sorry. Please enter numeric values.\n\n"
			sys.exit()

	def process_values(self):
		self.flight_ids = map(lambda x: "Flight #" + str(x), xrange(self.total_flights))
		self.frieght_ids = map(lambda x: "Freight #" + str(x), xrange(self.total_freights))
		self.merged_ids = self.flight_ids + self.frieght_ids
		print "Total: ", self.merged_ids


	def pending_ids(self, merged_ids):
		self.toggle_in_queue(self.picked_ele)
		self.get_random()

	def push_ele(self, ele_name):
		print "Allowed: {0}".format(ele_name)

	def clear_all(self):
		if self.in_queue:
			self.push_ele(self.in_queue)
		if self.picked_ele:
			self.push_ele(self.picked_ele)
		sys.exit("\n******** Successfully Completed!! ********")

	def toggle_in_queue(self, picked_ele):

		if not self.merged_ids:
			self.clear_all()

		if self.in_queue:
			if "Flight" in self.picked_ele:
				self.push_ele(self.picked_ele)
				self.push_ele(self.in_queue) 
				self.in_queue = None
			else:
				self.push_ele(self.in_queue)
				self.push_ele(self.picked_ele)
				self.in_queue = None
		else:
			if "Freight" in self.picked_ele:
				print "Queued: {0}".format(self.picked_ele)
				self.in_queue = self.picked_ele
				# Wait for second ele using get_random()
			else:
				# print "\nLast: Flight", self.in_queue
				self.push_ele(self.picked_ele)
		self.get_random()


	def get_random(self):
		'''To pick a random of All ids'''
		# print "\n In get_random()"
		if self.merged_ids:
			self.picked_ele = random.choice(self.merged_ids)
			print "\nRequest: {0}".format(self.picked_ele)
			# print "\nself.merged_ids: ", self.merged_ids
			self.merged_ids.remove(self.picked_ele)
			self.pending_ids(self.merged_ids)

	def begin(self):
		self.input_values()
		self.process_values()
		self.get_random()

c = Clearance()
c.begin()