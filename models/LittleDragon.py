from models.Monster import Monster

class LittleDragon (Monster):

    def __init__(self):
        super().__init__()
        self.bonus_end = 1
        self.gold_amount = self.calculate_gold_amount()
        self.leather_amount = self.calculate_leather_amount()