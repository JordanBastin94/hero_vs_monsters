from abc import ABC, abstractmethod
from models.Dice import Dice

class Character(ABC):
    def __init__(self):
        self.bonus_str = 0
        self.bonus_end = 0
        self._str = self.calculate_stat()
        self._end = self.calculate_stat()
        self._max_hp = self.calculate_base_hp()
        self.actual_hp = self.max_hp
        

    @property
    def str(self):
        return self._str

    @property
    def end(self):
        return self._end

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def actual_hp(self):
        return self._actual_hp

    @actual_hp.setter
    def actual_hp(self, nv_hp):
        if type(nv_hp) != int :
            raise TypeError("New hp quantity must be of type integer !")
        self._actual_hp = nv_hp

    @property
    def bonus_str(self):
        return self._bonus_str

    @bonus_str.setter
    def bonus_str(self,nv_str):
        if type(nv_str) != int:
            raise TypeError("The new bonus strength amount must be of type integer !")
        self._bonus_str = nv_str

    @property
    def bonus_end(self):
        return self._bonus_end

    @bonus_end.setter
    def bonus_end(self, nv_end):
        if type(nv_end) != int :
            raise TypeError('The new endurance amount must be of type integer !')
        self._bonus_end = nv_end

    @property
    def is_alive(self):
        return self.actual_hp > 0

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
        total_end = self.end + self.bonus_end
        if total_end < 5 :
            bonus = -1
        elif total_end < 10 :
            bonus = 0
        elif total_end < 15 :
            bonus = 1
        else :
            bonus = 2

        return (total_end+bonus)

    def strike(self, enemy : Character):
        dice = Dice(1,4)
        hit_power = dice.throw()
        total_str = self.str + self.bonus_str
        if total_str < 5 :
            hit_power -= 1
        elif total_str < 10:
            pass
        elif total_str < 15:
            hit_power += 1
        else :
            hit_power += 2

        enemy.actual_hp -= hit_power

    def __str__(self):
        return f"{self.__class__.__name__} : STR = {self.str + self.bonus_str}, END = {self.end+self.bonus_end}, HP = {self.max_hp}"