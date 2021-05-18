from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()


    def set_name(self):
        self.name = input("Enter player name? (human class)")  # test. remove player class
        return self.name


    def choose_gesture(self):
        chosen_gesture = input(f'Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, or {self.gestures[4]} (from human)')
        if chosen_gesture in self.gestures:
            self.chosen_gesture = chosen_gesture
            print(f'{self.name} chooses {self.chosen_gesture}.')
            return self.chosen_gesture
        else:
            self.choose_gesture()


    # player = Player()
    # player.name = input("Enter player name? (human class)")


    # def set_name(self):
    #     self.name = input("What is your name?")
    #     return self.name


    # def choose_gesture(self):
        # choose gesture with input