from models.Monster import Monster

class Wolf (Monster):
    def __init__(self):
        super().__init__()
        self.leather_amount = self.calculate_leather_amount()