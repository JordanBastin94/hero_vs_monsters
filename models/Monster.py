from models.Character import Character
from models.Dice import Dice
from abc import ABC

class Monster(Character, ABC) :

    def __init__(self):
        super().__init__()
        self.gold_amount = 0
        self.leather_amount = 0

    @property
    def gold_amount(self):
        return self._gold_amount

    @gold_amount.setter
    def gold_amount(self, nv_amount):
        if type(nv_amount) != int :
            raise TypeError("The new amonut of gold must be an integer !")
        self._gold_amount = nv_amount

    @property
    def leather_amount(self):
        return self._leather_amount

    @leather_amount.setter
    def leather_amount(self, nv_amount):
        if type(nv_amount) != int :
            raise TypeError("The new amount of leather must be of type ineger !")
        self._leather_amount = nv_amount

    def calculate_gold_amount(self):
        dice = Dice(1,6)
        return dice.throw()

    def calculate_leather_amount(self):
        dice = Dice(1,4)
        return dice.throw()