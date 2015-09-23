
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
		max_index = int(len(list) - 1)
		while min_index <= max_index:
			midpoint = int((min_index + max_index) / 2)
			if target == list[midpoint]:
				return midpoint
			elif target < list[midpoint]:
				max_index = midpoint - 1
			elif target > list[midpoint]:
				min_index = midpoint + 1
		return -1

	# Overthinking things: 
	def inner_binary(self, list, target, min_index, max_index):
		midpoint = int((max_index + min_index) / 2)

		if max_index - min_index > 0:
			if target == list[midpoint]:
				return midpoint
			elif target < list[midpoint]:
				new_max = midpoint - 1
				return self.inner_binary(list, target, min_index, new_max)
			elif target > list[midpoint]:
				new_min = midpoint + 1
				return self.inner_binary(list, target, new_min, max_index)
			else:
				return "fail"
		else:
			return -1

	def rec_binary(self, list, target):
		# assumption that list is already sorted
		min_index = 0
		max_index = len(list) - 1

		index = self.inner_binary(list, target, min_index, max_index)
		return index
