from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()


    player = Player()
    player.name = input("Enter player name? (human class)")


    # def set_name(self):
    #     self.name = input("What is your name?")
    #     return self.name


    # def choose_gesture(self):
        # choose gesture with input