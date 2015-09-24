
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
		# List is sorted
		min_index = 0
		max_index = len(list) - 1
		while min_index <= max_index:
			midpoint = ((max_index - min_index) // 2) + min_index # integer division
			if target == list[midpoint]:
				return midpoint
			elif target < list[midpoint]:
				max_index = midpoint - 1
			elif target > list[midpoint]:
				min_index = midpoint + 1
		return -1
