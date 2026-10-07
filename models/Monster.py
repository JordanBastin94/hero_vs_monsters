from models.Character import Character
from models.Dice import Dice
from abc import ABC

class Monster(Character, ABC) :

    def __init__(self):
        super().__init__()
        self._gold_amount = 0
        self._leather_amount = 0

    @property
    def gold_amount(self):
        return self._gold_amount

    @property
    def leather_amount(self):
        return self._leather_amount

    def calculate_gold_amount(self):
        dice = Dice(1,6)
        return dice.throw()

    def calculate_leather_amount(self):
        dice = Dice(1,4)
        return dice.throw()