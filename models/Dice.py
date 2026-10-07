import random

class Dice :
    #CONSTRUCTOR
    def __init__(self, min, max):
        self._min = min
        self._max = max

    #GETTER
    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    #FUNCTION
    def throw(self):
        return random.randint(self.min, self.max)

    