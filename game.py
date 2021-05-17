import ai
import human
from player import Player
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or AI()

    def run_game(self):
        # self.welcome_message()
        self.choose_game_type()
        # make sure both player objects exist and input name, if necessary
        pass

    def welcome_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!\n")
        print("Instructions to the game:\n")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock\n")
        print("Best of three wins!\n")

    def choose_game_type(self):
        while True:
            try:
                game_type = int(input("Choose game type: (1) Player vs Player or (2) Player vs AI"))
            except ValueError:
                continue
            if game_type == 1:
                self.player_one = human.Human.set_name(self)
                print(f'Hello {self.player_one}')
                self.player_two = human.Human.set_name(self)
                print(f'Hello {self.player_two}')
                print(f'{self.player_one} vs {self.player_two}.')
                break
            elif game_type == 2:
                self.player_one = human.Human.set_name(self)
                print(f'Hello {self.player_one}')
                self.player_two = ai.AI.set_name(self)
                print(f'Hello {self.player_two}')
                print(f'{self.player_one} vs {self.player_two}.')
                break


    def game_round(self):  # Loop until one side wins best of 3
        pass

    def display_winner(self):
        pass