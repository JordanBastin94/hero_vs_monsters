from models.Hero import Hero

class Dwarf (Hero):

    def __init__(self):
        super().__init__()
        self.bonus_end = 2