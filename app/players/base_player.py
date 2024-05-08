
from typing import List

from constants import NUM_GOODS_TO_GOLD
from good import Good
from game import GameManager
from app.stall import Stall


class Player:
    def __init__(self, name: str, game_manager: GameManager):
        self.name = name
        self.score = 0
        self.goods = []
        self.cups = []
        self.game_manager = game_manager

        self.dice_colour_to_action = {
            "red": self.buy_good,
            "orange": self.buy_good,
            "blue": self.buy_good,
            "yellow": self.buy_good,
            "green": self.trade,
            "black": self.buy_cup_move_bazaar,
        }

    def roll_dice_get_options(self) -> tuple[List[callable], List[str]]:
        dice = self.game_manager.dice
        options = []
        colours = list(dice.roll())

        for colour in colours:
            if not colour in self.dice_colour_to_action:
                raise Exception(f"Invalid dice colour {colour}")
            options.append(self.dice_colour_to_action[colour])
        options.append(self.sell_goods)
        return (options, colours)
    
    def take_turn(self):
        raise NotImplementedError("Subclasses must implement this method")

    def sell_goods(self, goods: List[Good], cups: int):
        # handle cups and goods
        num_goods = len(goods)

        total_num_wares = num_goods + cups

        if total_num_wares not in NUM_GOODS_TO_GOLD:
            raise Exception(f"Invalid number of wares being sold {total_num_wares}")
        
        gold = NUM_GOODS_TO_GOLD[total_num_wares]

        if cups > self.cups:
            raise Exception(f"player has {self.cups} cups, but trying to sell {cups} cups")
        
        for good in goods:
            if good not in self.goods:
                raise Exception(f"Good {good.colour} not in player's goods")
            self.goods.remove(good)
            self.game_manager.stalls.get_stall(good.colour).add_good(good)

        for _ in range(cups):
            self.game_manager.bazaar.add_cup()
            self.cups -= 1

        self.score += gold

    def buy_good(self, colour: str):
        stall = self.game_manager.get_stall(colour)
        if stall.isBazaared:
            raise Exception(f"Stall {colour} has is currently bazaared")
        
        if not stall.goods:
            raise Exception(f"No goods in stall {colour}, choose a differnt stall") # todo: handle this later
        good = stall.goods.pop()
        self.goods.append(good)
        self.score -= 1

    def trade():
        # TODO: implement this
        pass

    def buy_cup_move_bazaar(self, move_bazaar_to_stall: Stall):
        bazaar = self.game_manager.bazaar
        bazaar.remove_cup()
        self.cups += 1
        if self.cups > 2:
            raise Exception("Too many cups")
        self.move_baazar(move_bazaar_to_stall)
        pass

    def move_baazar(self, move_bazaar_to_stall: Stall):
        if self.game_manager.bazaar.current_stall:
            self.game_manager.bazaar.current_stall.isBazaared = False
        self.game_manager.bazaar.current_stall = move_bazaar_to_stall
        move_bazaar_to_stall.isBazaared = True
        pass
