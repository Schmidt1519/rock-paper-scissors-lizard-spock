class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.chosen_gesture = ''
        self.score = 0


    def set_name(self):
        self.name = input("Enter player name? (player class)")
        return self.name


    def choose_gesture(self):
        chose_gesture = input(f'Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, or {self.gestures[4]}')
        if chose_gesture in self.gestures:
            self.chosen_gesture = chose_gesture
        else:
            self.choose_gesture()


# while True:
#     try:
#         self.chosen_gesture = int(input(f'Choose your gesture: (1) {self.gestures[0]}, (2) {self.gestures[1]}, (3){self.gestures[2]}, {self.gestures[3]}, or {self.gestures[4]}')
#     except ValueError:
#         continue
#     if self.chosen_gesture == 1: