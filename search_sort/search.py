
class Searches:

    def linear(self, list, target):
        for i, value in enumerate(list):
            if value == target:
                return i

        # Didn't find what we're looking for
        return -1

    def binary(self, list, target):
        # set mid
        min = 0
        max = len(list) - 1


        while min <= max:
            # Else, if the halfway point is > or < target:
            # Greater than: divide right half of list
            mid = (min + max) // 2
            print(list[mid])
            if list[mid] == target:
                return mid
            elif list[mid] > target:
                min = mid + 1
                print("Bigger")

            else:
                # Less than: divide left half of list
                max = mid - 1

        print(min, max, mid)

        # Didn't find what we were looking for
        return -1
