from models.Character import Character
from abc import ABC

class Hero(Character, ABC) :

    def __init__(self):
        super().__init__()
        self.gold_stock = 0
        self.leather_stock = 0

    @property
    def gold_stock(self):
        return self._gold_stock

    @gold_stock.setter
    def gold_stock(self, quantity):
        if type(quantity) != int :
            raise TypeError('Gold quantity must be of type integer !')
        elif quantity >= 0:
            raise ValueError("Gold quantity can't be negative !")
        self._gold_stock = quantity

    @property
    def leather_stock(self):
        return self._leather_stock

    @leather_stock.setter
    def leather_stock(self, quantity):
        if type(quantity) != int :
            raise TypeError('Leather quantity must be of type integer !')
        elif quantity >= 0:
            raise ValueError("Leather quantity can't be negative !")
        self._leather_stock = quantity


    #Fonction
    def regenerate_hp(self):
        self.actual_hp = self.max_hp