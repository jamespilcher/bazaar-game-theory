
from typing import List
from bazaar import Bazaar
from constants import STALL_COLOURS, WIN_GOLD_AMOUNT
from app.players.base_player import Player
from dice import Dice
from app.stall import Stall


class GameManager:
    def __init__(self):
        self.players = []
        self.current_player = 0
        self.bazaar = Bazaar(self)
        self.dice = Dice()
        self.stalls = [Stall(colour) for colour in STALL_COLOURS]
        self.game_over = False

    def get_stall(self, colour: str):
        for stall in self.stalls:
            if stall.colour == colour:
                return stall
        raise Exception(f"Stall not found {colour}")

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.current_player]

    def get_player(self, index):
        return self.players[index]

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)

    def get_winner(self):
        for player in self.players:
            if player.get_score() >= WIN_GOLD_AMOUNT:
                return player
        return None

    def get_scores(self):
        return [player.get_score() for player in self.players]

    def get_scores_and_names(self):
        return [(player.get_name(), player.get_score()) for player in self.players]

    def get_scores_and_names_sorted(self):
        return sorted(self.get_scores_and_names(), key=lambda x: x[1], reverse=True)

    def get_scores_sorted(self):
        return sorted(self.get_scores(), reverse=True)

    def get_scores_and_names_with_rank(self):
        scores_and_names = self.get_scores_and_names_sorted()
        return [(i + 1, scores_and_names[i][0], scores_and_names[i][1]) for i in range(len(scores_and_names))]

    def get_scores_with_rank(self):
        scores = self.get_scores_sorted()
        return [(i + 1, scores[i]) for i in range(len(scores))]

    def initialize(self, players: List[Player]):
        self.players = players

    def play(self):
        while not self.game_over:
            player = self.get_current_player()
            player.take_turn()
            self.next_player()
            if self.get_winner():
                self.game_over = True
        return self.get_winner()