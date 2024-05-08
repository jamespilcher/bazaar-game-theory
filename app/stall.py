
from constants import GOODS_PER_STALL
from good import Good


class Stall:
    def __init__(self, colour: str):
        self.colour = colour
        self.isBazaared = False
        self.goods = [Good(colour) for _ in range(GOODS_PER_STALL)]

    def get_goods(self):
        return self.goods
    
    def add_good(self, good: Good):
        self.goods.append(good)
    
    def remove_good(self, good: Good):
        self.goods.remove(good)
