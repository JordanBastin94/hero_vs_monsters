from models.Monster import Monster

class Orc (Monster): 

    def __init__(self):
        super().__init__()
        self.bonus_str = 1
        self.gold_amount = self.calculate_gold_amount()