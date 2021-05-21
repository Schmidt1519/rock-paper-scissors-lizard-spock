from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__()


    def set_name(self):
        self.name = "The Bot"


    def choose_gesture(self):
        print(f'Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, or {self.gestures[4]}')
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} chooses {self.chosen_gesture}.')