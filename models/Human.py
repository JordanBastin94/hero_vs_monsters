from models.Hero import Hero

class Human (Hero):

    def __init__(self):
        super().__init__()
        self.bonus_str = 1
        self.bonus_end = 1