
class Searches:

    def linear(self, list, target):
        # lopp over each item in the list
        for index, item in enumerate(list):
            if item == target:
                return index
        return -1

    def binary(self, list, target):
        min = 0
        max = len(list) - 1
        while max >= min:
            mid = (max + min) / 2
            if list[mid] == target:
                return mid
            elif list[mid] < target:
                # move midpoint to upper/right half
                min = mid + 1
            else:
                # move midpoint to lower/left half
                max = mid - 1
