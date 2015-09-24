
class Searches:

    def linear(self, list, target):
    	for i, value in enumerate(list):
    		if value == target:
    			return i




    	return -1       

def binary(self, list, target):
	first = 0
	last = len(list)-1
	found = False
	
	while first <= last and not found:
		midpoint = (first + last)//2
		if list[midpoint] == target:
			found = True

		elif target < list[midpoint]:
				last = midpoint - 1
		
		else:
			first = midpoint + 1
			
			return found
