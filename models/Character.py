from abc import ABC, abstractmethod
from models.Dice import Dice

class Character(ABC):
    def __init__(self):
        self._str = self.calculate_stat()
        self._end = self.calculate_stat()
        self.hp = self.calculate_base_hp()

    @property
    def str(self):
        return self._str

    @property
    def end(self):
        return self._end

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,nv_hp):
        if type(nv_hp) != int :
            raise TypeError('new hp must be of type integer !')
        self._hp = nv_hp


    #FONCTION
    def calculate_stat(self):
        dice = Dice(1,6)
        lowest = 7
        total = 0
        for i in range(4):
            throw = dice.throw()

            if throw < lowest :
                lowest = throw

            total += throw

        return total-lowest

    def calculate_base_hp(self):
        bonus = 0
        if self.end < 5 :
            bonus = -1
        elif self.end < 10 :
            bonus = 0
        elif self.end < 15 :
            bonus = 1
        else :
            bonus = 2

        return (self.end+bonus)