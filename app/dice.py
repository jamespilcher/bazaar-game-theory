import random
class Dice:
    def __init__(self):
        self.dice_color_mapping = {
            1: ('red', 'blue'),
            2: ('red', 'green'),
            3: ('green', 'orange'),
            4: ('orange', 'blue'),
            5: ('green', 'black'),
            6: ('black')
        }

    def roll(self) -> tuple[str]:
        return self.dice_color_mapping[random.randint(1, 6)]