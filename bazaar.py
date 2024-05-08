
class Bazaar:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.num_cups = 2
        self.current_stall = None

    def remove_cup (self):
        self.num_cups -= 1
        if self.num_cups < 0:
            raise Exception("No more cups left")
        
    def add_cup(self):
        self.num_cups += 1
        if self.num_cups > 2:
            raise Exception("Too many cups")
