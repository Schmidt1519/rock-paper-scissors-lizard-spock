from player import Player
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or AI()

    def run_game(self):
        # welcome_message()
        # choose_game_type()
        # make sure both player objects exist and input name, if necessary
        pass

    def welcome_message(self):
        # welcome message / rules
        pass

    def choose_game_type(self):  # (1) Player vs Player or (2) Player vs AI
        pass

    def game_round(self):  # Loop until one side wins best of 3
        pass

    def display_winner(self):
        pass