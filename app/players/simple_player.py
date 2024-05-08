
from base_player import Player


class SimplePlayer(Player):
    def __init__(self):
        super().__init__("SimplePlayer")
    
    def take_turn(self):
        options, colours = self.roll_dice_get_options()
        for option in options:
            option()
        self.game_manager.next_player()