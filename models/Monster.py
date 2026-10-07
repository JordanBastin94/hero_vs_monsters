from models.Character import Character
from models.Dice import Dice
from abc import ABC

class Monster(Character, ABC) :

    def calculate_gold_amount(self):
        dice = Dice(1,6)
        return dice.throw()

    def calculate_leather_amount(self):
        dice = Dice(1,4)
        return dice.throw()