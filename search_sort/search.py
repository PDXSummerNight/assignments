
class Searches:

	def linear(self, list, target):
		i = 0
		while i < len(list):
			if list[i] == target:
				return i
			else: 
				i += 1 
		return -1

		# for i, value in enumerate(list):
		# 	if list[i] == target:
		# 		return i
		# return -1


	def binary(self, list, target):
		# assumption that list is already sorted
		pass

