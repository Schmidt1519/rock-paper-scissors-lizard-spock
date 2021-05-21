from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.welcome_message()
        self.choose_game_type()
        self.game_round()
        self.display_winner()

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
                self.player_two = Human()
                self.player_one.set_name()
                print(f'Hello {self.player_one.name}.')
                self.player_two.set_name()
                print(f'Hello {self.player_two.name}.')
                print(f'{self.player_one.name} vs {self.player_two.name}.')
                break
            elif game_type == 2:
                self.player_two = AI()
                self.player_one.set_name()
                print(f'Hello {self.player_one.name}.')
                self.player_two.set_name()
                print(f'Hello {self.player_two.name}.')
                print(f'{self.player_one.name} vs {self.player_two.name}.')
                break


    def game_round(self):
        while self.player_one.score < 2 and self.player_two.score < 2:

            print('\nNew Round:\n')

            self.player_one.choose_gesture()
            self.player_two.choose_gesture()

            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
               print('Round tie.')

            elif self.player_one.chosen_gesture == self.player_one.gestures[0] and self.player_two.chosen_gesture == self.player_two.gestures[2]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[0] and self.player_two.chosen_gesture == self.player_two.gestures[3]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[1] and self.player_two.chosen_gesture == self.player_two.gestures[0]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[1] and self.player_two.chosen_gesture == self.player_two.gestures[4]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[2] and self.player_two.chosen_gesture == self.player_two.gestures[1]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[2] and self.player_two.chosen_gesture == self.player_two.gestures[3]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[3] and self.player_two.chosen_gesture == self.player_two.gestures[1]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[3] and self.player_two.chosen_gesture == self.player_two.gestures[4]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[4] and self.player_two.chosen_gesture == self.player_two.gestures[0]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            elif self.player_one.chosen_gesture == self.player_one.gestures[4] and self.player_two.chosen_gesture == self.player_two.gestures[2]:
                print(f'{self.player_one.name} wins the round.')
                self.player_one.score += 1

            else:
                print(f'{self.player_two.name} wins the round.')
                self.player_two.score += 1

            print(f'\nScoreboard:  {self.player_one.name}: {self.player_one.score}.  {self.player_two.name}: {self.player_two.score}.')

    def display_winner(self):
        if self.player_one.score >= 2:
            print(f"\n{self.player_one.name} wins the match!")
        if self.player_two.score >= 2:
            print(f"\n{self.player_two.name} wins the match!")