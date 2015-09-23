
class Searches:

    def linear(self, list, target):
        for i, value in enumerate(list):
            if value == target:
                return i

        # Didn't find what we're looking for
        return -1

    def binary(self, list, target):
        pass
